import galtea
def main():

    galtea.create_annotation_task(name="text-eval",
                                    template_type="ab_testing",
                       specific_id="id",
                       dataset_path="./dataset.json",
                       fields=["prompt", "answer_a", "answer_b"],
                       metadata_fields=["model_a"])

if __name__ == "__main__":
    main()