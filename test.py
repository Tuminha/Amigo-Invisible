import unittest
from amigo_invisible import assign_friends, participants
import os
import json
from unittest.mock import patch, MagicMock
from app import load_json_file, print_participants, handle_participant_input, display_assigned_participants
import streamlit as st

if 'participants' not in st.session_state:
    st.session_state['participants'] = []


class TestAssignFriends(unittest.TestCase):
    def setUp(self):
        # Mock the test.json file before each test
        self.mock_json_file = MagicMock()
        self.mock_json_file.__enter__.return_value = self.mock_json_file
        self.mock_open = patch('builtins.open', return_value=self.mock_json_file).start()

    def tearDown(self):
        patch.stopall()

    def test_assign_friends(self):
        # Test that the function assigns a friend to each participant
        assignments = assign_friends(participants)
        self.assertEqual(len(assignments), len(participants))

    def test_no_self_assignment(self):
        # Test that the function does not assign a participant to themselves
        assignments = assign_friends(participants)
        for participant, friend in assignments.items():
            self.assertNotEqual(participant, friend)

    def test_no_repeated_assignment(self):
        # Test that the function does not assign a friend to multiple participants
        assignments = assign_friends(participants)
        friends = list(assignments.values())
        for friend in friends:
            self.assertEqual(friends.count(friend), 1)

    def test_update_json_file(self):
        # Test that the function updates the assignments.json file correctly
        # Mock a test.json file
        assignments = assign_friends(participants)
        self.mock_json_file.write.assert_called_once_with(json.dumps(assignments))

    def test_load_json_file(self):
        # Test that the function loads the assignments.json file correctly
        # Mock a test.json file
        assignments = assign_friends(participants)
        self.mock_json_file.read.return_value = json.dumps(assignments)
        file_assignments = load_json_file('test.json')
        # Check that the assignments were loaded correctly
        self.assertEqual(assignments, file_assignments)
        
    def test_print_participants(self):
        # Test that the function prints the participants correctly
        # Mock a test.json file
        assignments = assign_friends(participants)
        self.mock_json_file.read.return_value = json.dumps(assignments)
        # Print the participants
        print_participants(1, participants, assignments)
        # Check that the participants were printed correctly
        self.assertEqual(assignments, assignments)
    
    def test_handle_participant_input(self):
        # Test that the function handles the participant input correctly
        # Mock a test.json file
        assignments = assign_friends(participants)
        self.mock_json_file.read.return_value = json.dumps(assignments)
        # Handle the participant input
        handle_participant_input(1)
        # Check that the participants were handled correctly
        self.assertEqual(assignments, assignments)

    def test_display_assigned_participants(self):
        # Mock a test.json file
        assignments = assign_friends(participants)
        self.mock_json_file.read.return_value = json.dumps(assignments)
        # Display the assigned participants
        display_assigned_participants('test.json')
        # Check that the participants were displayed correctly
        self.assertEqual(assignments, assignments)

if __name__ == '__main__':
    unittest.main()