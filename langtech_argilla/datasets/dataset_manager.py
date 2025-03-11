import logging

import argilla as rg

from langtech_argilla.templates.template import Template
from langtech_argilla.utils import load_json, sanitize_string

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("argilla_operations.log"), logging.StreamHandler()],
)


class DatasetManager:
    def __init__(self, client: rg.Argilla, dataset=None):
        self._client = client
        self.dataset = dataset

    def create_dataset(self, name: str, workspace: rg.Workspace, settings: dict):
        """
        Create a dataset.
        Parameters:
            name (str): The name of the dataset.
            workspace (rg.Workspace): The workspace where the dataset will be created.
            settings (dict): The settings of the dataset.
        """

        dataset_name = f"{sanitize_string(name)}"

        existing_dataset = self._client.datasets(
            name=dataset_name, workspace=workspace.name
        )

        if not existing_dataset:

            dataset = rg.Dataset(
                name=dataset_name,
                workspace=workspace,
                settings=settings,
                client=self._client,
            ).create()

            logging.info(f"Dataset {dataset_name} created.")

            self.dataset = dataset
        else:
            logging.error(
                f"Dataset {dataset_name} already exists in workspace {workspace.name}"
            )
            self.dataset = existing_dataset

    def upload_records(self, template: Template, dataset_path: str):
        """Load the records of the dataset from a JSON file.
        Parameters:
            template (Template): The template to use to validate the records.
            dataset_path (str): The path to the JSON file containing the records.
        """
        data = load_json(dataset_path)
        records = []

        for item in data:
            # Validate fields based on template model
            validated_fields = template.fields_model.model_validate(item)

            # Extract fields dynamically based on the template model
            fields = {
                field: getattr(validated_fields, field)
                for field in validated_fields.model_fields.keys()
                if field not in ["id", "metadata"]
            }

            record = rg.Record(
                id=validated_fields.id,
                fields=fields,
                metadata=(
                    validated_fields.metadata
                    if hasattr(validated_fields, "metadata")
                    else None
                ),
            )
            records.append(record)

        self.dataset.records.log(records=records)

    def export_records(self, dataset_name: str, workspace_name: str, output_path: str):
        """Export the records of the dataset to a JSON file."""
        self._get_dataset(dataset_name, workspace_name)
        self.dataset.records.to_json(output_path)

    def get_progress(self, dataset_name: str, workspace_name: str):
        """Get the progress of the dataset."""
        self._get_dataset(dataset_name, workspace_name)

        return self.dataset.progress()

    def _get_dataset(self, dataset_name: str, workspace_name: str) -> rg.Dataset:
        if not self.dataset or type(self.dataset) == str:
            self.dataset = self._client.datasets(dataset_name, workspace_name)
            if not self.dataset:
                raise ValueError(
                    f"Dataset {dataset_name} not found in workspace {workspace_name}"
                )

    @classmethod
    def get_dataset_manager(
        cls, client: rg.Argilla, dataset_name: str, workspace_name: str
    ):
        """
        Get the DatasetManager instance for a given dataset.
        """

        try:
            dataset = client.datasets(name=dataset_name, workspace=workspace_name)
            return cls(client, dataset)

        except Exception as e:
            raise ValueError(
                f"Dataset {dataset_name} not found in workspace {workspace_name}"
            ) from e
