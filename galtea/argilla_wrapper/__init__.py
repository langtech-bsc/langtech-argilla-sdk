from typing import List, Optional

from galtea.argilla_wrapper.datasets.dataset_manager import DatasetManager
from galtea.argilla_wrapper.templates.concrete import ConcreteTemplateFactory
from galtea.argilla_wrapper.users.user_manager import UserManager
from galtea.argilla_wrapper.workspaces.workspace_manager import WorkspaceManager



def create_annotation_task(name, template_type, dataset_path):
    workspace_manager = WorkspaceManager()
    workspace = workspace_manager.create_workspace(name)

    user_manager = UserManager()
    user_manager.create_users(workspace)

    template_factory = ConcreteTemplateFactory()
    template = template_factory.get_template(name, template_type)
    settings = template.build_settings()
    
    dataset_manager = DatasetManager(template)
    dataset_manager.create_dataset(name, workspace, settings)
    dataset_manager.load_records(dataset_path=dataset_path)


