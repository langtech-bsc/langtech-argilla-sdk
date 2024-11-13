from dotenv import load_dotenv
load_dotenv()

from galtea.workspaces.workspace_manager import WorkspaceManager
from galtea.connection.sdk_connection import SDKConnection


sdk_connection = SDKConnection()
workspace_manager = WorkspaceManager(client=sdk_connection.client)
workspace = workspace_manager.create_workspace(name="example-workspace")