# Debugging Exercise Generator - LLM Fine-tuning Logic

This repository contains all the logic used to develop an experimental fine-tuned LLM that generates debugging exercises.

## How the Model Works
Learning to debug effectively is tough, and takes lots of practice. The idea of the model is to help introductory programming educators to develop lots of debugging exercises quickly. Currently, the system prompt is "":

The user then inputs the following, formatted in XML:
- A description for a programming problem.
- A correct solution to that problem.
- The number of syntax errors they would like to add to the correct solution.
- The number of runtime errors they would like to add to the correct solution.
- The number of logical errors they would like to add to the correct solution.

The total number of errors to add must be at least 1.

The model then outputs the following:

- A bugged program with the specified number of errors added, based on research into common novice programming mistakes.
- An explanation of each error added, including the line number of each error.

## Repository Details
The repository contains the following directories.
- **content**: The programming exercises used to generate training and testing data. Each programming exercise contains a description and a correct Python solution.
- **fine-tuning-examples**: The example user and assistant responses used to train and test the model, split into training and test examples. For each example, the user response is stored in the user folder, and the assistant response is stored in the assistant folder. Each exercise is numbered.

The full training and testing examples, stored in valid jsonl with system, user, and assistant prompts, are stored in the fine_tuning_training_parsed.jsonl and fine_tuning_testing_parsed.jsonl files. These are automatically generated when the create_fine_tuning_examples.py Python script is run

## Contributing

Feel free to fork this repository to add some of your own fine-tuning examples. I suggest you do this by the following:
1. Add some programming exercises.
2. Add a few fine-tuning examples for that exercise. I try to add a few training examples per programming exercise, as I think adding lots of examples for a single programming exercises may cause overfitting.
3. Create the new jsonl files. Do this by running the create_fine_tuning_examples.py (changing the number_training_examples and number_test_examples accordingly).
4. Submit a fine-tuning job!

Happy fine-tuning!