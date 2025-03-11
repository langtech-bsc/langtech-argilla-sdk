import logging
from argparse import ArgumentParser

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
        "--usernames",
        type=str,
        required=True,
        help="A list of usernames to add (name1,name2,name3...)",
    )
    parser.add_argument(
        "--workspace-name",
        type=str,
        required=True,
        help="Name of the workspace you want to add users to",
    )
    args = parser.parse_args()
    usernames = args.usernames
    workspace_name = args.workspace_name

    users = usernames.strip().split(",")

    connection = SDKConnection()
    client = connection.get_client()

    workspace_manager = WorkspaceManager(client)
    if not workspace_manager.workspace_exists(workspace_name):
        workspace_manager.create_workspace(workspace_name)

    workspace = client.workspaces(workspace_name)

    for user in users:
        user_manager = UserManager(client)
        user_manager.add_user_to_workspace(user, workspace)


if __name__ == "__main__":
    main()
