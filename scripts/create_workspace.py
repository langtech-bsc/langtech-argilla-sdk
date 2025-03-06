import logging
from argparse import ArgumentParser

from galtea.connection.sdk_connection import SDKConnection
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
    args = parser.parse_args()
    workspace_name = args.workspace_name

    connection = SDKConnection()
    client = connection.get_client()

    workspace_manager = WorkspaceManager(client)

    if not workspace_manager.workspace_exists(workspace_name):
        workspace_manager.create_workspace(workspace_name)
        logging.info(f"Workspace {workspace_name} created.")
    else:
        logging.error(f"Workspace {workspace_name} already exists.")


if __name__ == "__main__":
    main()
