from dotenv import load_dotenv
load_dotenv()

import galtea


def main():
    
    with galtea.ArgillaAnnotationTask() as pipeline:

        pipeline.create_annotation_task(
            name="text-eval",
            template_type="ab_testing",
            dataset_path="./sample_data/dataset.json",
            min_submitted=1,
            guidelines="This is a test guidelines",
            users_path_file="./sample_data/users.json"
        )

        # print(pipeline.get_progress())
    
if __name__ == "__main__":
    main()