from typing import List, Optional
import argilla as rg 
from .template import Template
class SimpleABTestingTemplate(Template):
    def __init__(self, name, fields: List[str], extra_fields: Optional[List[rg.Field]] = None, guidelines: Optional[str] = None):
        self.name = name        
        self.ab_fields = fields

        self.guidelines = guidelines
        self.extra_fields = extra_fields
       

    def build_settings(self):

        rg_fields = [
            rg.TextField(name=field, title=field, required=True)
            for field in self.ab_fields
        ]

        if self.extra_fields is not None:
            rg_fields.extend(self.extra_fields)

        settings = rg.Settings(
            allow_extra_metadata=True,
            guidelines=self.guidelines,
            fields=rg_fields,
            questions=[
                rg.LabelQuestion(
                    name="label",
                    title="What is the best response given the prompt?",
                    description="Select the one that applies.",
                    required=True,
                    labels={"answer_a": "Answer A", "answer_b": "Answer B", "both": "Both", "none": "None"}
                ),
            ]
        )


        return settings
        