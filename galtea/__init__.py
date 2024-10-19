from typing import List, Optional

from galtea.argilla_wrapper.data.dataset_manager import DatasetManager
from galtea.argilla_wrapper.templates.concrete import ConcreteTemplateFactory
from galtea.argilla_wrapper.users.user_manager import UserManager
from galtea.argilla_wrapper.workspaces.workspace_manager import WorkspaceManager



def create_annotation_task(name, template_type, dataset_path, specific_id, fields, metadata_fields: Optional[List] = None):
    user_manager = UserManager()
    user = user_manager.create_default_user(name)

    workspace_manager = WorkspaceManager()
    workspace = workspace_manager.create_workspace(name)
    
    user_manager.add_user_to_workspace(user.username, workspace)
    
    template_factory = ConcreteTemplateFactory()
    template = template_factory.get_template(name, fields,template_type)
    settings = template.build_settings()
    
    dataset_manager = DatasetManager()
    dataset_manager.create_dataset(name, workspace, settings)
    dataset_manager.load_records(dataset_path=dataset_path,specific_id=specific_id, fields=fields, metadata_fields=metadata_fields)


