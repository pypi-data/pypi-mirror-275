# ProofOfTraining Python SDK

The ProofOfTraining Python SDK provides a convenient way to interact with the ProofOfTraining smart contract on the blockchain network. It allows you to submit and retrieve model metadata using the ProofOfTraining protocol.

## Installation

To install the ProofOfTraining Python SDK, use the following command:

```
pip install proof-of-training
```

## Usage

### Initializing the ProofOfTraining object

To start using the ProofOfTraining SDK, you need to create an instance of the `ProofOfTrain` class by providing the following parameters:

- `rpc_url`: The RPC URL of the blockchain network to connect for submitting and verifying metadata.
- `public_key`: The public key of the user, used to identify the sender of the transactions.
- `private_key`: The private key of the user, used for signing transactions to ensure security and authenticity.

```python
from proof_of_training import ProofOfTraining

rpc_url = "https://rpc.testnet.rss3.io"
public_key = "0x1234567890123456789012345678901234567890"
private_key = "your-private-key"

pot = ProofOfTraining(rpc_url, public_key, private_key)
```

### Submitting Model Metadata

To submit model metadata to the blockchain, use the `submit_proof` method of the `ProofOfTrain` object. This method takes the following parameters:

- `model_id`: The unique identifier of the model.
- `metadata`: An instance of `ModelMetadata` containing the model's metadata.
- `gas` (optional): The gas limit for the transaction (default: 500000).
- `gas_price` (optional): The gas price in gwei (default: 50).
- `wait_for_receipt` (optional): Whether to wait for the transaction to be confirmed (default: False).

```python
from proof_of_training import ModelMetadata

model_id = "your-model-id"
metadata = ModelMetadata(
    model_name="Model Name",
    model_md5="d4c2e8a2b3cb1a9c0a7b7f4c5a9a3b2e",
    model_url="https://huggingface.co/bert-base-uncased",
    dataset_url="https://huggingface.co/datasets/glue",
    training_params={"epochs": 3, "batch_size": 32},
    training_date="2024-05-27",
    model_version="1.0",
    author="Hugging Face",
    description="BERT base model, uncased version, trained on the GLUE dataset."
)

tx_hash = pot.submit_proof(model_id, metadata, wait_for_receipt=False)
print(f"Transaction hash: {tx_hash}")
```

If `wait_for_receipt` is set to `False` (which is the default), the `submit_proof` method will return the transaction hash. You can use this hash to track the status of the transaction later.

If `wait_for_receipt` is set to `True`, the method will wait for the transaction to be confirmed on the blockchain and return the transaction receipt.

```python
tx_receipt = pot.submit_proof(model_id, metadata, wait_for_receipt=True)
print(f"Transaction receipt: {tx_receipt}")
```

### Retrieving Model Metadata

To retrieve the metadata for a specific model from the blockchain, use the `get_proof` method of the `ProofOfTrain` object. This method takes the `model_id` parameter, which is the unique identifier of the model.

```python
model_id = "your-model-id"
metadata = pot.get_proof(model_id)

if metadata:
    print(f"Model ID: {model_id}")
    print(f"Model Name: {metadata.model_name}")
    print(f"Model MD5: {metadata.model_md5}")
    print(f"Model URL: {metadata.model_url}")
    print(f"Dataset URL: {metadata.dataset_url}")
    print(f"Training Params: {metadata.training_params}")
    print(f"Training Date: {metadata.training_date}")
    print(f"Model Version: {metadata.model_version}")
    print(f"Author: {metadata.author}")
    print(f"Description: {metadata.description}")
else:
    print(f"Model with ID {model_id} not found.")
```

## Error Handling

The SDK handles common errors that may occur during the interaction with the blockchain network. If an error occurs, an appropriate exception will be raised with a descriptive error message.

## License

This SDK is released under the [MIT License](LICENSE).

## Contributing

Contributions to the ProofOfTraining Python SDK are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/RSS3-Network/pot).
