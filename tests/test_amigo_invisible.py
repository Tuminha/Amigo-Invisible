import unittest
from amigo_invisible.amigo_invisible import assign_secret_friend, check_in, participants, participant_numbers
import json
from unittest.mock import patch, MagicMock, mock_open

class TestAmigoInvisible(unittest.TestCase):
    def test_assign_secret_friend_logic(self):
        # Call assign_secret_friend and check if assignments are unique and valid
        assignments = assign_secret_friend()
        self.assertEqual(len(assignments), len(participants))  # All participants should be assigned

        for key, value in assignments.items():
            # Check if the secret friend is not the same as the participant
            self.assertNotEqual(key, participant_numbers[value["secret_friend"]])

    def test_check_in_function(self):
        # Manually create a sample assignments dictionary
        sample_assignments = {
            str(num): {"secret_friend": "Some Friend", "checked": False}
            for num in participant_numbers.values()
        }

        # Test check_in with an assigned participant
        participant_number = list(participant_numbers.values())[0]
        with patch('builtins.open', mock_open(read_data=json.dumps(sample_assignments))):
            response = check_in(participant_number)
            self.assertIn("Check-in successful", response)

        # Test re-check-in with the same participant
        sample_assignments[str(participant_number)]["checked"] = True
        with patch('builtins.open', mock_open(read_data=json.dumps(sample_assignments))):
            response = check_in(participant_number)
            self.assertIn("already checked in", response)

        # Test check_in with a non-existent participant
        with patch('builtins.open', mock_open(read_data=json.dumps({}))):
            response = check_in(participant_number)
            self.assertIn("not been assigned", response)

if __name__ == '__main__':
    unittest.main()
