"""
This module contains the tests for the amigo_invisible module.
We will test the functionality of the functions in the amigo_invisible module and test different situations like:
- The number entered is not in the list of participants
- The number entered is already in the assignements file
- The number entered is not in the assignements file
- The number entered is in the assignements file but the secret friend assigned is not in the list of participants
- After a full round of secret friend assignements, there are no more potential secret friends available and everyone has an assigned secret friend and no one is left out
- There is no repeated secret friend assigned

We will also consider the following:
- Test Initialization and Cleanup: We will add a setup method (setUp) to initialize any common prerequisites for our tests, such as creating a mock environment or setting initial values. Similarly, a teardown method (tearDown) will be used to clean up after tests, like deleting temporary files or resetting states.
- Edge Cases and Exception Handling: We will include tests for edge cases, such as when input values are at the boundary of what's expected (e.g., very large or small numbers). We will also test how the functions handle exceptions or unexpected errors, such as read/write errors with the assignements.json file.
- Input Validation: We will add tests for input validation, ensuring that the functions behave correctly with various types of input (e.g., non-numeric values, negative numbers, etc.).
- Test for Idempotency: We will verify that repeated execution of functions with the same inputs yields consistent results, which is especially important for functions that alter files or data.
- Performance Testing (Optional): Although it might not be a primary concern for our project, considering simple performance tests (like how the system performs under a large number of participants) can be insightful.
- Documentation and Readability: While our introduction is clear, we will ensure that each test function also has a docstring explaining what specific aspect it's testing. We will make sure to follow the Python style guide (PEP 8) for consistency and readability.
- Mocking External Dependencies: If we haven't planned this already, we will remember to mock external dependencies like file I/O to avoid creating, reading, or writing actual files during testing.
- Randomness in Tests: Since our code uses randomness (random secret friend assignment), we will consider how we will handle this in tests. We might need to mock or control the random behavior to make our tests predictable and repeatable.
"""

import unittest
from unittest.mock import patch, MagicMock
from amigo_invisible.amigo_invisible import assign_secret_friend, check_in, participants, participant_numbers
import json
from unittest.mock import mock_open


class TestAmigoInvisible(unittest.TestCase):
    def setUp(self):
        # Mock the os.path.exists to always return True
        self.path_exists_patcher = patch('os.path.exists', return_value=True)
        self.mock_path_exists = self.path_exists_patcher.start()

        # Mock the json.load to return an empty dictionary initially
        self.json_load_patcher = patch('json.load', return_value={})
        self.mock_json_load = self.json_load_patcher.start()

        # Mock the json.dump to just pass
        self.json_dump_patcher = patch('json.dump')
        self.mock_json_dump = self.json_dump_patcher.start()

        # Mock the open function
        self.open_patcher = patch('builtins.open', mock_open(read_data='{}'))
        self.mock_open = self.open_patcher.start()

    def tearDown(self):
        self.path_exists_patcher.stop()
        self.json_load_patcher.stop()
        self.json_dump_patcher.stop()
        self.open_patcher.stop()

    @patch('amigo_invisible.amigo_invisible.random.choice')
    def test_multiple_interaction_rounds(self, mock_random_choice):
        # Define the number of rounds
        num_rounds = 5
        counter = [0]  # Create a list to store the counter
        all_rounds_assignments = [] # Create a dictionary to store the assignments for all rounds

        for _ in range(num_rounds):
            # Reset the mock file for each round
            self.mock_open.return_value = MagicMock(read_data='{}')
            self.mock_json_load.return_value = {}

            def side_effect(participants_list):
                # Use counter[0] to access the first element of the list, which acts as our counter
                result = participants_list[counter[0] % len(participants_list)]
                counter[0] += 1  # Increment the counter
                return result

            mock_random_choice.side_effect = side_effect

            # Assign a secret friend to each participant and check for no errors
            for number in participant_numbers.values():
                result = assign_secret_friend(number)
                self.assertNotIn("Error", result)
                self.assertNotIn("Invalid", result)
                self.assertNotIn("No potential", result)

            # Check-in each participant and verify no errors
            for number in participant_numbers.values():
                result = check_in(number)
                self.assertNotIn("Error", result)
                self.assertNotIn("Invalid", result)
                self.assertIn("Check-in successful", result)

            # Simulate the assignments as they would be in the 'assignments.json' file
            simulated_assignments = {
                # simulate the assignments structure here:
                "1": "2",
                "2": "3",
                "3": "4",
                "4": "5",
                "5": "1"
            }
            all_rounds_assignments.append(simulated_assignments)

            # Debug print
            round_number = counter[0] - 1

            print(f"Round {round_number + 1} assignments:")  # Debug print
            print(simulated_assignments)  # Debug print

            # Increment the counter for the next round
            counter[0] += 1
            # Debug print to show all assignments after all rounds
            print("All rounds assignments:")
            print(all_rounds_assignments)

        # Stop mocking open here to write to the actual file system
            self.open_patcher.stop()

            # After all rounds, write the all_rounds_assignments to a JSON file
            report_path = "/Users/franciscoteixeirabarbosa/Downloads/all_rounds_assignments_report.json"
            with open(report_path, "w", encoding='utf-8') as f:
                json.dump(all_rounds_assignments, f, ensure_ascii=False, indent=4)

            # Optionally, print the report to the console
            print(json.dumps(all_rounds_assignments, ensure_ascii=False, indent=4))

            # Function to confirm the json file was printed and to which file
            print(f"Report printed to {report_path}")

            # Restart the open patcher if needed for other tests
            self.open_patcher.start()

if __name__ == '__main__':
    unittest.main()
