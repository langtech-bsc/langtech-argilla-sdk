import galtea
def main():

    galtea.create_annotation_task(
        name="text-eval",
        template_type="ab_testing",
        dataset_path="./dataset.json",
    )
                      
if __name__ == "__main__":
    main()