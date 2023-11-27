import unittest
from amigo_invisible import assign_secret_friend, participant_numbers
import os
import json
from unittest.mock import patch, MagicMock
import streamlit as st

if 'participants' not in st.session_state:
    st.session_state['participants'] = []


class TestAssignSecretFriend(unittest.TestCase):
    def setUp(self):
        # Mock the test.json file before each test
        self.mock_json_file = MagicMock()
        self.mock_json_file.__enter__.return_value = self.mock_json_file
        self.mock_open = patch('builtins.open', return_value=self.mock_json_file).start()

    def tearDown(self):
        patch.stopall()

    def test_assign_secret_friend(self):
        # Test that the function assigns a secret friend to each participant
        for number in participant_numbers.values():
            secret_friend = assign_secret_friend(number)
            self.assertIn(secret_friend, participant_numbers.keys())

    def test_no_self_assignment(self):
        # Test that the function does not assign a participant to themselves
        for number in participant_numbers.values():
            secret_friend = assign_secret_friend(number)
            self.assertNotEqual(participant_numbers[secret_friend], number)

    def test_update_json_file(self):
        # Test that the function updates the assignements.json file correctly
        # Mock a test.json file
        for number in participant_numbers.values():
            secret_friend = assign_secret_friend(number)
        self.mock_json_file.write.assert_called()

    def test_load_json_file(self):
        # Test that the function loads the assignements.json file correctly
        # Mock a test.json file
        for number in participant_numbers.values():
            secret_friend = assign_secret_friend(number)
        self.mock_json_file.read.assert_called()

if __name__ == '__main__':
    unittest.main()
