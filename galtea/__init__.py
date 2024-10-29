from typing import List, Optional
from .argilla_wrapper import create_annotation_task as _create_annotation_task


def create_annotation_task(name, template_type, dataset_path, min_submitted: Optional[int] = 1, guidelines: Optional[str] = None):
    return _create_annotation_task(name, template_type, dataset_path, min_submitted, guidelines)
