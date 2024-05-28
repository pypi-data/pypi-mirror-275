import json
import os
from typing import Union

from web3 import Web3
from web3.exceptions import ContractLogicError
from web3.middleware import geth_poa_middleware
from web3.types import TxReceipt

from proof_of_training.model_metadata import ModelMetadata


def _load_contract_abi():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{current_dir}/abi.json") as abi_file:
        return json.load(abi_file)


class ProofOfTraining:
    def __init__(self, rpc_url, public_key, private_key):
        """
        Initialize the ProofOfTraining object.

        :param rpc_url: The RPC URL of the blockchain network to connect for submitting and verifying metadata.
        :param public_key: The public key of the user, used to identify the sender of the transactions.
        :param private_key: The private key of the user, used for signing transactions to ensure security and authenticity.
        """
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.web3.is_connected():
            raise ConnectionError("Unable to connect to the blockchain network")

        # For networks like Rinkeby or other testnets using PoA
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)

        self.public_key = public_key
        self.private_key = private_key

        self.contract_address = "0xeCe62b3838746983916fFBFc5C97237206dbFE83"
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=_load_contract_abi())  # type: ignore

    def submit_proof(
        self, model_id: str, metadata: ModelMetadata, gas: int = 500000, gas_price: int = 50, wait_for_receipt: bool = False
    ) -> Union[str, TxReceipt]:
        """
        Submit the model metadata to the blockchain.

        This method should implement the logic for interacting with the blockchain network through the RPC URL,
        including creating, signing, and submitting transactions that encapsulate the model metadata.

        :param model_id: The unique identifier of the model.
        :param metadata: An instance of ModelMetadata containing the model's metadata.
        :param gas: The gas limit for the transaction (default: 500000).
        :param gas_price: The gas price in gwei (default: 50).
        :param wait_for_receipt: Whether to wait for the transaction to be confirmed (default: True).
        :return: The transaction hash if wait_for_receipt is False, otherwise the transaction receipt.
        """
        nonce = self.web3.eth.get_transaction_count(self.public_key)
        model_id_bytes32 = Web3.to_bytes(text=model_id).ljust(32, b"\0")
        tx = self.contract.functions.submitProof(model_id_bytes32, json.dumps(metadata.to_dict())).build_transaction(
            {"chainId": self.web3.eth.chain_id, "gas": gas, "gasPrice": self.web3.to_wei(gas_price, "gwei"), "nonce": nonce, "from": self.public_key}
        )

        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        if not wait_for_receipt:
            return self.web3.to_hex(tx_hash)

        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        if tx_receipt.status == 0:
            raise ValueError(f"Transaction failed with status {tx_receipt.status}")

        return tx_receipt

    def get_proof(self, model_id: str) -> ModelMetadata | None:
        """
        Retrieve the metadata for a specified model from the blockchain.

        This method implements the logic for querying the blockchain records through the RPC URL to obtain
        the metadata corresponding to the given model ID.

        :param model_id: The unique identifier of the model.
        :return: The metadata details or None if not found.
        """
        try:
            model_id_bytes32 = Web3.to_bytes(text=model_id).ljust(32, b"\0")
            metadata_json = self.contract.functions.getProof(model_id_bytes32).call()
            if not metadata_json:
                return None
            return ModelMetadata.from_dict(json.loads(metadata_json))
        except ContractLogicError as e:
            if "Model not found" in str(e):
                print(f"Model with ID {model_id} not found.")
                return None
            else:
                print(f"An unexpected error occurred: {e}")
                raise e
