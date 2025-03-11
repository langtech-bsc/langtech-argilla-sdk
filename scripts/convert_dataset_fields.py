import json

# Load the JSON file
input_file = "example_datasets/ab_testing_100_red_team.json"
output_file = "example_datasets/ab_testing_100_red_team_updated.json"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)  # Load the JSON list

# Rename fields for each record
for record in data:
    record["id"] = record.pop("instance_id")
    record["answer_a"] = record.pop("answer_A")
    record["answer_b"] = record.pop("answer_B")
    record["model_a"] = record.pop("model_A")
    record["model_b"] = record.pop("model_B")

# Save the transformed JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated JSON saved to {output_file}")
