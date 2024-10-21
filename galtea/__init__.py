from typing import List, Optional
from .argilla_wrapper import create_annotation_task as _create_annotation_task


def create_annotation_task(name, template_type, dataset_path, specific_id, fields, metadata_fields: Optional[List] = None):
    return _create_annotation_task(name, template_type, dataset_path, specific_id, fields, metadata_fields)
