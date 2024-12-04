from dotenv import load_dotenv
load_dotenv()

from galtea.datasets.dataset_manager import DatasetManager
from galtea.connection.sdk_connection import SDKConnection


sdk_connection = SDKConnection()
dataset_manager = DatasetManager.get_dataset_manager(client=sdk_connection.client, dataset_name="text-eval", workspace_name="text-eval")

print(dataset_manager.get_progress())
