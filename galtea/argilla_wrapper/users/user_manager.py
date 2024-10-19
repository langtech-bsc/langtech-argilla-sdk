from galtea.argilla_wrapper.utils import generate_random_string, sanitize_string
from ..connection.sdk_connection import SDKConnection
import argilla as rg
class UserManager:
    def __init__(self):
        self.connection = SDKConnection()

    def create_default_user(self, name, role="annotator"):
        # Logic to create random user using the SDK
        username = sanitize_string(f"{name}_default_user")
        password = generate_random_string(12)
        
        user = self.connection._instance.users(username)

        if user is not None:
            print(f"User {username} already exists")
            return user
        
        user_to_create = rg.User(
            username=username,
            password=password,
            first_name="Default",
            last_name="User",
            role=role,
            client=self.connection._instance
        )
        user = user_to_create.create()

        print(f"User details: username: {user.username} \n password: {password}")
        return user_to_create

    def create_user(self, username, password, first_name, last_name, role="annotator"):
        # Logic to create user using the SDK
        
        username = sanitize_string(username)

        user = self.connection._instance.users(username)

        if user is not None:
            return
        user_to_create = rg.User(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=role,
            client=self.connection._instance
        )
        
        return user_to_create.create()


    def _create_bulk_users_from_csv(self, csv_path):
        pass
        
    

    def add_user_to_workspace(self, username, workspace: rg.Workspace):

        user = self.connection._instance.users(username)

        if user is None:
            raise ValueError(f"User {username} does not exist")


        if user in workspace.users:
            print(f"User {username} is already in workspace {workspace.name}")
            return
        

        try:
            user.add_to_workspace(workspace)
            print(f"User {username} added to workspace {workspace.name}")
            return

        except Exception as e:
            print(f"Error adding user {username} to workspace {workspace.name}: {e}")
            return
        