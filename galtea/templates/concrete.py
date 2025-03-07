from typing import Optional

from galtea.models.template_fields import TemplateType
from galtea.templates.creator import TemplateFactory
from galtea.templates.simple_ab_testing import SimpleABTestingTemplate


class ConcreteTemplateFactory(TemplateFactory):
    def get_template(
        self,
        template_type: TemplateType,
        min_submitted: Optional[int] = 1,
        guidelines: Optional[str] = None,
    ):
        if template_type == TemplateType.ab_testing:
            return SimpleABTestingTemplate(min_submitted, guidelines)
        else:
            raise ValueError(f"Unknown template type: {template_type.value}")
