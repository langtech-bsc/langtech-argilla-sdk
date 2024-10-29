# Galtea Annotation Task Creator

Streamline your text evaluation process with Galtea's powerful annotation task creator.

## Setting Up the Development Environment

1. Clone the repository:
   ```
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -e .
   ```

4. Set up your environment variables:
   Create a `.env` file in your project root directory with the following content:

   ```
   ARGILLA_API_URL=your_argilla_api_url
   ARGILLA_API_KEY=your_argilla_api_key
   ```

   Replace `your_argilla_api_url` and `your_argilla_api_key` with your actual Argilla API URL and key.

## Creating Annotation Tasks

Elevate your text evaluation process with Galtea's intuitive annotation task creator. Here's how to get started:

1. Prepare your dataset:
   Ensure you have a JSON dataset file (e.g., `ab_testing_100_red_team.json`) in your project directory.
   Follow the specific json schema format for the dataset.

   Example:
   ```json
      [
         {
            "id": "1",
            "prompt": "This is a prompt",
            "answer_a": "This is answer a",
            "answer_b": "This is answer b",
            "metadata": {
               "model_a": "model_a_value",
               "model_b": "model_b_value",
               "extra_metadata_field": "extra_metadata_field_value"
            }
         },
         {
            "id": "2",
            "prompt": "This is another prompt",
            "answer_a": "This is answer a",
            "answer_b": "This is answer b",
            "metadata": {
               "model_a": "model_a_value",
               "model_b": "model_b_value",
               "extra_metadata_field": "extra_metadata_field_value"
            }
         },
         {
            "id": "3",
            "prompt": "This is a third prompt",
            "answer_a": "This is answer a",
            "answer_b": "This is answer b",
            "metadata": {
               "model_a": "model_a_value",
               "model_b": "model_b_value",
               "extra_metadata_field": "extra_metadata_field_value"
            }
         }
      ]
      
   ```

2. Create your annotation task:
   In your `main.py` file, use the following code to create a simple ab testing annotation task:

   ```python
   import galtea

   def main():
       galtea.create_annotation_task(
           name="text-eval",
           template_type="ab_testing",
           dataset_path="./ab_testing_100_red_team.json",
           min_submitted=1,
           guidelines="This is a test guidelines"
       )

   if __name__ == "__main__":
       main()
   ```

3. Launch your annotation task:
   Run the script to create your task:
   ```
   python main.py
   ```

This will generate a powerful "text-eval" annotation task using the AB testing template. The task will leverage your specified dataset and include the fields "prompt", "answer_a", and "answer_b", with "model_a" as a metadata field.

Customize the parameters to align with your specific evaluation needs, such as adjusting the `name`, `dataset_path`, `fields`, and `metadata_fields`.

With Galtea, you're now ready to supercharge your text evaluation process and gain valuable insights from your data!
