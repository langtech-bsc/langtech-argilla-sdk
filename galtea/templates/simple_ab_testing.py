from typing import Optional

import argilla as rg

from galtea.models.template_fields import ABTestingFields
from galtea.templates.template import Template


class SimpleABTestingTemplate(Template):
    def __init__(
        self, min_submitted: Optional[int] = 1, guidelines: Optional[str] = ""
    ):
        self.guidelines = (
            guidelines
            if guidelines
            else """
            1. **Consistency:** Label each example consistently according to the defined criteria, ensuring no bias towards either variant.
            2. **Clarity:** Focus on the specific elements being tested (e.g., text, design) and how they impact the user's experience.
            3. **Detail:** Provide brief but clear justifications for your choice if required, highlighting key differences.
            4. **Neutrality:** Avoid letting personal preferences influence your annotation; stick to the test's objective.
        """
        )
        self.fields_model = ABTestingFields
        self.min_submitted = min_submitted

    def build_settings(self):
        """DATASET SETTINGS"""
        settings = rg.Settings(
            distribution=rg.TaskDistribution(min_submitted=self.min_submitted),
            allow_extra_metadata=True,
            guidelines=self.guidelines,
            fields=[
                rg.TextField(
                    name="prompt",
                    title="Prompt",
                    use_markdown=True,
                    required=True,
                    description="Field description",
                ),
                rg.TextField(
                    name="answer_a",
                    title="Answer A",
                    use_markdown=True,
                    required=True,
                    description="Field description",
                ),
                rg.TextField(
                    name="answer_b",
                    title="Answer B",
                    use_markdown=True,
                    required=True,
                    description="Field description",
                ),
            ],
            questions=[
                rg.LabelQuestion(
                    name="label",
                    title="What is the best response given the prompt?",
                    description="Select the one that applies.",
                    required=True,
                    labels={
                        "answer_a": "Answer A",
                        "answer_b": "Answer B",
                        "both": "Both",
                        "none": "None",
                    },
                ),
                rg.RatingQuestion(
                    name="rating",
                    values=[1, 2, 3, 4, 5],
                    title="How satisfied are you with the response?",
                    description="1 = very unsatisfied, 5 = very satisfied",
                    required=True,
                ),
                rg.TextQuestion(
                    name="text",
                    title="Copy and modify the response here if there is anything you would like to modify.",
                    description="If there is anything you would modify in the response copy and edit the response in this field.",
                    use_markdown=True,
                    required=False,
                ),
            ],
        )
        return settings
