import logging
from argparse import ArgumentParser

from langtech_argilla.connection.sdk_connection import SDKConnection
from langtech_argilla.datasets.dataset_manager import DatasetManager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("argilla_operations.log"), logging.StreamHandler()],
)


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "--dataset-name",
        type=str,
        required=True,
        help="Name of the dataset you want to create",
    )
    parser.add_argument(
        "--workspace-name",
        type=str,
        required=True,
        help="Name of the workspace you want to create",
    )
    args = parser.parse_args()
    dataset_name = args.dataset_name
    workspace_name = args.workspace_name

    connection = SDKConnection()
    client = connection.get_client()

    dataset_manager = DatasetManager(client)
    dataset_manager.delete_dataset(dataset_name, workspace_name)


if __name__ == "__main__":
    main()
