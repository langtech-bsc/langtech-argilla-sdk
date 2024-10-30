from typing import Optional
from galtea.argilla_wrapper.templates.simple_ab_testing import SimpleABTestingTemplate
from galtea.argilla_wrapper.templates.creator import TemplateFactory

class ConcreteTemplateFactory(TemplateFactory):
    def get_template(self, name: str, template_type: str, min_submitted: Optional[int] = 1, guidelines: Optional[str] = None):
        if template_type == "ab_testing":
            return SimpleABTestingTemplate(name, min_submitted, guidelines)
        else:
            raise ValueError(f"Unknown template type: {template_type}")
