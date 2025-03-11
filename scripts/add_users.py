import logging
from argparse import ArgumentParser
from pathlib import Path

from langtech_argilla.connection.sdk_connection import SDKConnection
from langtech_argilla.users.user_manager import UserManager
from langtech_argilla.workspaces.workspace_manager import WorkspaceManager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("argilla_operations.log"), logging.StreamHandler()],
)


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "--users-file",
        type=str,
        required=True,
        help="Path to users data",
    )
    parser.add_argument(
        "--workspace-name",
        type=str,
        required=True,
        help="Name of the workspace you want to create",
    )
    args = parser.parse_args()
    users_file = Path(args.users_file)
    workspace_name = args.workspace_name

    connection = SDKConnection()
    client = connection.get_client()

    workspace_manager = WorkspaceManager(client)
    if not workspace_manager.workspace_exists(workspace_name):
        workspace_manager.create_workspace(workspace_name)

    workspace = client.workspaces(workspace_name)

    user_manager = UserManager(client)
    user_manager.create_users(workspace, users_file)


if __name__ == "__main__":
    main()
