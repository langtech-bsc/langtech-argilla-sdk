from galtea.argilla_wrapper.utils import sanitize_string
from ..connection.sdk_connection import SDKConnection
import argilla as rg

class WorkspaceManager:
    def __init__(self):

        self.connection = SDKConnection()


    def workspace_exists(self, workspace_name: str) -> bool:

        workspace = self.connection._instance.workspaces(name=workspace_name)

        if workspace:
            return True

        return False

    """
    Given a workspace name, create a new workspace if it doesn't exist
    :param name: name of the workspace
    :return: workspace object
    
    """
    def create_workspace(self, name):

        name = sanitize_string(name)
        
        if self.workspace_exists(name):
            print(f"Workspace {name} already exists")
            return self.connection._instance.workspaces(name=name)
        
        workspace = rg.Workspace(
            name=name,
            client=self.connection._instance
        )

        workspace.create()

        return workspace