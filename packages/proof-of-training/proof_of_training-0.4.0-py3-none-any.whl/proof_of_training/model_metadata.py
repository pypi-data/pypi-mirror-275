class ModelMetadata:
    def __init__(
        self,
        model_name,
        model_md5,
        model_url,
        dataset_url,
        training_params=None,
        training_date=None,
        model_version=None,
        author=None,
        description=None,
    ):
        """
        Initialize the model metadata.

        :param model_name: The name of the model.
        :param model_md5: The MD5 hash value of the model, used to uniquely identify the model.
        :param model_url: The URL where the trained model is stored.
        :param dataset_url: The URL of the dataset used for training the model.
        :param training_params: The parameters used for training the model, such as number of epochs, batch size, etc.
        :param training_date: The date when the model was trained.
        :param model_version: The version of the model, useful for tracking model iterations.
        :param author: The author or entity responsible for training the model.
        :param description: A brief description of the model, including its purpose and any other relevant information.
        :param protocol_version: The protocol version of the metadata structure.
        """
        self.model_md5 = model_md5
        self.model_name = model_name
        self.model_url = model_url
        self.dataset_url = dataset_url
        self.training_params = training_params
        self.training_date = training_date
        self.model_version = model_version
        self.author = author
        self.description = description
        self.protocol_version = ("1.0.0",)

    @classmethod
    def from_dict(cls, data):
        """
        Create a ModelMetadata instance from a dictionary.

        :param data: A dictionary containing the model metadata.
        :return: A ModelMetadata instance.
        """
        return cls(
            model_md5=data.get("model_md5"),
            model_name=data.get("model_name"),
            model_url=data.get("model_url"),
            dataset_url=data.get("dataset_url"),
            training_params=data.get("training_params"),
            training_date=data.get("training_date"),
            model_version=data.get("model_version"),
            author=data.get("author"),
            description=data.get("description"),
        )

    def to_dict(self):
        """
        Convert the ModelMetadata instance to a dictionary.

        :return: A dictionary representation of the ModelMetadata instance.
        """
        return {
            "model_md5": self.model_md5,
            "model_name": self.model_name,
            "model_url": self.model_url,
            "dataset_url": self.dataset_url,
            "training_params": self.training_params,
            "training_date": self.training_date,
            "model_version": self.model_version,
            "author": self.author,
            "description": self.description,
            "protocol_version": self.protocol_version,
        }
