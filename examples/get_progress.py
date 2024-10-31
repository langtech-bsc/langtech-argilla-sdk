from dotenv import load_dotenv
load_dotenv()

from galtea.argilla_wrapper.datasets.dataset_manager import DatasetManager
from galtea.argilla_wrapper.connection.sdk_connection import SDKConnection


sdk_connection = SDKConnection()
dataset_manager = DatasetManager.get_dataset_manager(client=sdk_connection.client, dataset_name="text-eval_dataset", workspace_name="text-eval")

print(dataset_manager.get_progress())
