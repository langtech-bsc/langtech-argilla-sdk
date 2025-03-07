import logging
from argparse import ArgumentParser

from galtea.connection.sdk_connection import SDKConnection
from galtea.datasets.dataset_manager import DatasetManager
from galtea.templates.simple_ab_testing import SimpleABTestingTemplate
from galtea.workspaces.workspace_manager import WorkspaceManager

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
        help="Name of the workspace you want to create",
    )
    parser.add_argument(
        "--dataset-name",
        type=str,
        required=True,
        help="Name of the dataset you want to create",
    )
    parser.add_argument(
        "--dataset-file",
        type=str,
        required=True,
        help="Path to dataset file",
    )
    parser.add_argument(
        "--min-annotations",
        type=int,
        required=False,
        default=1,
        help="Number of annotations each sample should receive",
    )
    args = parser.parse_args()
    workspace_name = args.workspace_name
    dataset_name = args.dataset_name
    dataset_file = args.dataset_file
    min_annotations = args.min_annotations

    connection = SDKConnection()
    client = connection.get_client()

    template = SimpleABTestingTemplate(min_submitted=min_annotations)
    settings = template.build_settings()

    workspace_manager = WorkspaceManager(client)
    if not workspace_manager.workspace_exists(workspace_name):
        workspace_manager.create_workspace(workspace_name)

    workspace = client.workspaces(workspace_name)

    dataset_manager = DatasetManager(client)
    dataset_manager.create_dataset(dataset_name, workspace, settings)
    dataset_manager.upload_records(template, dataset_file)


if __name__ == "__main__":
    main()
