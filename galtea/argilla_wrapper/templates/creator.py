from abc import ABC, abstractmethod

class TemplateFactory(ABC):
    @abstractmethod
    def get_template(self, template_type: str):
        pass

