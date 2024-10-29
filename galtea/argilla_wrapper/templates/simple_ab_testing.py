from typing import List, Optional
import argilla as rg

from galtea.argilla_wrapper.models.ab_testing_fields import ABTestingFields 
from .template import Template
class SimpleABTestingTemplate(Template):
    def __init__(self, name, guidelines: Optional[str] = None, distribution: Optional[int] = 1):
        self.name = name        
        self.guidelines = guidelines
        self.fields_model = ABTestingFields  # Add this line
        # self.distribution = distribution

    def build_settings(self):

        settings = rg.Settings(
            allow_extra_metadata=True,
            guidelines=self.guidelines,
            # distribution=self.distribution,
            fields=[
                rg.TextField(name="prompt", title="Prompt", required=True),
                rg.TextField(name="answer_a", title="Answer A", required=True),
                rg.TextField(name="answer_b", title="Answer B", required=True),
            ],
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
        