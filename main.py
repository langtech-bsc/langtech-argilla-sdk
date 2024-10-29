import galtea


def main():

    galtea.create_annotation_task(
        name="text-eval",
        template_type="ab_testing",
        dataset_path="./dataset.json",
        min_submitted=1,
        guidelines="This is a test guidelines"
    )
                      
if __name__ == "__main__":
    main()