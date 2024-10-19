
from galtea.argilla_wrapper.connection.sdk_connection import SDKConnection
from galtea.argilla_wrapper.utils import load_json, sanitize_string
import argilla as rg

class DatasetManager:
    def __init__(self):
        self.connection = SDKConnection()
        self.template = None
    def create_dataset(self, name, workspace: rg.Workspace, settings):
        
        dataset_name = f"{sanitize_string(name)}_dataset"

        existent_dataset = self.connection._instance.datasets(name=dataset_name, workspace=workspace.name)

        if existent_dataset is not None:
            print(f"Dataset {dataset_name} already exists in workspace {workspace.name}")
            self.dataset = existent_dataset
            return

        dataset = rg.Dataset(
            name=dataset_name,
            workspace=workspace,
            settings=settings,
            client=self.connection._instance
        ).create()

        print(f"Dataset {dataset_name} created.")

        self.dataset = dataset

    def load_records(self, dataset_path, specific_id, fields, metadata_fields):
        data = load_json(dataset_path)
        records = []

        for item in data:
            
            _fields = {key.lower():item[key] for key in item.keys() if key in fields}
            metadata = {key.lower():item[key] for key in item.keys() if key in metadata_fields}

            record = rg.Record(
                id = item[specific_id],
                fields = _fields,
                metadata = metadata,
                )
        
            records.append(record)

        self.dataset.records.log(records=records)
        