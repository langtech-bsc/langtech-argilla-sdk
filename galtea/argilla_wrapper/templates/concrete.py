from galtea.argilla_wrapper.templates.simple_ab_testing import SimpleABTestingTemplate
from .creator import TemplateFactory

class ConcreteTemplateFactory(TemplateFactory):
    def get_template(self, name, template_type: str):
        if template_type == "ab_testing":
            return SimpleABTestingTemplate(name)
        else:
            raise ValueError(f"Unknown template type: {template_type}")
