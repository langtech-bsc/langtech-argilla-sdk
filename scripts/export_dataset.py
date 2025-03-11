import logging
from argparse import ArgumentParser

from langtech_argilla.connection.sdk_connection import SDKConnection
from langtech_argilla.datasets.dataset_manager import DatasetManager
from langtech_argilla.workspaces.workspace_manager import WorkspaceManager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("argilla_operations.log"), logging.StreamHandler()],
)


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "--workspace-name",
        type=str,
        required=True,
        help="Name of the workspace where the dataset is",
    )
    parser.add_argument(
        "--dataset-name",
        type=str,
        required=True,
        help="Name of the dataset you want to export",
    )
    parser.add_argument(
        "--export-path",
        type=str,
        required=True,
        help="Path where you want dataset exported to",
    )
    args = parser.parse_args()
    workspace_name = args.workspace_name
    dataset_name = args.dataset_name
    export_path = args.export_path

    connection = SDKConnection()
    client = connection.get_client()

    workspace_manager = WorkspaceManager(client)
    if not workspace_manager.workspace_exists(workspace_name):
        raise ValueError(f"Worksapce {workspace_name} not found!")

    dataset_manager = DatasetManager(client)
    dataset_manager.export_records(dataset_name, workspace_name, export_path)


if __name__ == "__main__":
    main()
