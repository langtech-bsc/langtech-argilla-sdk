from galtea.argilla_wrapper.connection.sdk_connection import SDKConnection
from galtea.argilla_wrapper.models.ab_testing_fields import ABTestingFields
from galtea.argilla_wrapper.models.base_fields import BaseTemplateFields
from galtea.argilla_wrapper.utils import load_json, sanitize_string
import argilla as rg
import time

class DatasetManager:
    def __init__(self, template):
        self.connection = SDKConnection()
        self.template = template
        self.dataset = None

    def create_dataset(self, name, workspace: rg.Workspace, settings):
        
        dataset_name = f"{sanitize_string(name)}_dataset"

        existent_dataset = self.connection._instance.datasets(name=dataset_name, workspace=workspace.name)

        if existent_dataset is not None:
            print(f"Dataset {dataset_name} already exists in workspace {workspace.name}")
            self.dataset = existent_dataset
            dataset_progress_data = self.dataset.progress()
            print(dataset_progress_data)
            if dataset_progress_data["completed"] == dataset_progress_data["total"]:
                print(f"Dataset {dataset_name} is already completed.")
                print(f"Exporting dataset to {dataset_name}_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json")
                self.dataset.records.to_json(f"{dataset_name}_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json")
            return

        dataset = rg.Dataset(
            name=dataset_name,
            workspace=workspace,
            settings=settings,
            client=self.connection._instance
        ).create()          

        print(f"Dataset {dataset_name} created.")

        self.dataset = dataset

    def load_records(self, dataset_path):
        data = load_json(dataset_path)
        records = []

        for item in data:
            # Validate fields based on template model
            validated_fields = self.template.fields_model.model_validate(item)
            
            # Extract fields dynamically based on the template model
            fields = {field: getattr(validated_fields, field) 
                     for field in validated_fields.model_fields.keys() 
                     if field not in ['id', 'metadata']}
            
            record = rg.Record(
                id=validated_fields.id,
                fields=fields,
                metadata=validated_fields.metadata if hasattr(validated_fields, 'metadata') else None,
            )
            records.append(record)

        self.dataset.records.log(records=records)
        
    def export_records(self, output_path):
        self.dataset.records.to_json(output_path)
