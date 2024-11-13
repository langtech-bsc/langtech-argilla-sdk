from dotenv import load_dotenv
load_dotenv()

from galtea.datasets.dataset_manager import DatasetManager
from galtea.connection.sdk_connection import SDKConnection


sdk_connection = SDKConnection()
dataset_manager = DatasetManager.get_dataset_manager(client=sdk_connection.client, dataset_name="dataset-name", workspace_name="example-workspace")

# Export the records to a JSON file
dataset_manager.export_records(output_path="./exported_records.json")