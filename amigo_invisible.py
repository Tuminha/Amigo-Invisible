import random
import json
import os

#This is a list of the participants in the game.
#👸 Mami, 🤦‍♀️ Maite, 😡 Marta, 👧🏻Oleia, 👦🏻Nuno, 👦🏼 Buis,🎅 Nicolas, 👶 Buarte, 👧 Matilda, 🚴 Lance, 🍆 Papi
participants = ["👸 Mami", "🤦‍♀️ Maite", "😡 Marta", "👧🏻 Oleia", "👦🏻 Nuno", "🚿 Buis","🎅 Nicolas", "👶 Buarte", "👧 Matilda", "🚴 Lance", "🍆 Papi"]


# This is a dictionary that stores the participant's name and the participant's number.
participant_numbers = {
    "👸 Mami": 69,
    "🤦‍♀️ Maite": 96,
    "😡 Marta": 66,
    "👧🏻 Oleia": 79,
    "👦🏻 Nuno": 98,
    "🚿 Buis": 11,
    "🎅 Nicolas": 27,
    "👶 Buarte": 20,
    "👧 Matilda": 99,
    "🚴 Lance": 23,
    "🍆 Papi": 68
}

# First a function that when a number from participant_numbers is entered, it randomly assigns a secret friend from the participants list.
# It also has to check if the assignements.json file exists and if it does, it has to create it the first time it is executed.
# The file should contain key values with the name, secret friend assigned and also a boolean to register that this person already checked in and already knows his her secret friend.
# The function should return the secret friend assigned and write it into the assignements.json file.
# Handling errors and also the case when the number entered is not in the list of participants should be considered, avoiding overwriting the file.
# The function should also return a message to the user with the name of the secret friend assigned.
# Save results in a file called assignements.json



def assign_secret_friend(number):
    """
    This function assigns a secret friend to a participant.
    It takes a number as input, checks if the number is in the list of participants,
    and if it is, it assigns a secret friend to the participant.
    The function also checks if the assignements.json file exists and if it does not,
    it creates it. The file contains key values with the name, secret friend assigned
    and also a boolean to register that this person already checked in and already knows his/her secret friend.
    The function returns the secret friend assigned and writes it into the assignements.json file.
    It handles errors and also the case when the number entered is not in the list of participants,
    avoiding overwriting the file. The function also returns a message to the user with the name of the secret friend assigned.
    """
    # Convert the number to a string
    str_number = str(number)

    # Check if the number is in the list of participants
    if number not in participant_numbers.values():
        return "Invalid participant number"

    # First check if the file exists
    if not os.path.exists("assignements.json"):
        # If it does not exist, create it
        assignements = {}
    else:
        # If it exists, open it and read it
        try:
            with open("assignements.json", "r", encoding='utf-8') as f:
                assignements = json.load(f)
        except Exception as e:
            return "Error reading assignements file: " + str(e)

    # If the number is already in the assignements file, return the secret friend assigned
    if str_number in assignements:
        return assignements[str_number]["secret_friend"]

    # If it is not, assign a secret friend and save it in the file.
    # The secret friend should be different from the person itself and also from the secret friend of the person itself
    def get_name(number):
        return list(participant_numbers.keys())[list(participant_numbers.values()).index(number)]
    
    def get_secret_friend(name):
        try:
            return assignements[participant_numbers[name]]["secret_friend"]
        except KeyError:
            return "Participant's name not found in assignments"

    # Create a list of potential secret friends, excluding the participant and their current secret friend
    potential_secret_friends = [friend for friend in participants if friend != get_name(number) and friend != get_secret_friend(get_name(number))]

    # If there are no potential secret friends, return an error message
    if not potential_secret_friends:
        return "No potential secret friends available"

    # Select a secret friend from the list of potential secret friends
    secret_friend = random.choice(potential_secret_friends)

    # Save the secret friend in the file
    assignements[str_number] = {"secret_friend": secret_friend, "checked": False}
    try:
        with open("assignements.json", "w", encoding='utf-8') as f:
            json.dump(assignements, f)
    except Exception as e:
        return "Error writing to assignements file: " + str(e)

    # Return the secret friend  
    return secret_friend
    
def check_in(number):
    """
    This function checks in a participant.
    It takes a number as input, checks if the number is in the list of participants,
    and if it is, it checks in the participant.
    The function also checks if the assignements.json file exists and if it does not,
    it returns an error message. If the file exists, it reads it and checks if the number is in the assignements.
    If the participant has already checked in, it returns a message.
    If the participant has not checked in, it updates the checked status to true and writes the updated data back to the file.
    The function returns a message to the user with the name of the secret friend assigned.
    """
    # Convert the number to a string
    number = str(number)

    # Check if the number is in the list of participants
    if int(number) not in participant_numbers.values():
        return "Invalid participant number"

    # Check if the file exists
    if not os.path.exists("assignements.json"):
        return "The assignements file does not exist"

    # If it exists, open it and read it
    try:
        with open("assignements.json", "r", encoding='utf-8') as f:
            assignements = json.load(f)
    except Exception as e:
        return "Error reading assignements file: " + str(e)

    # Check if the number is in the assignements
    if number not in assignements:
        return "The participant has not been assigned a secret friend"

    # If the participant has already checked in, return a message
    if assignements[number]["checked"]:
        return "The participant has already checked in and knows the secret friend that is {}".format(assignements[number]["secret_friend"])

    # If the participant has not checked in, update the checked status to true
    assignements[number]["checked"] = True

    # Write the updated data back to the file
    try:
        with open("assignements.json", "w", encoding='utf-8') as f:
            json.dump(assignements, f)
    except Exception as e:
        return "Error writing to assignements file: " + str(e)

    # Return a message to the user with the name of the secret friend assigned
    participant_name = [name for name, num in participant_numbers.items() if num == int(number)][0]
    return "Check-in successful for participant number {}, that corresponds to {}".format(number, participant_name)


# First assign a secret friend to participant number 69
print(assign_secret_friend(96))
# Then check-in participant number 69
print(check_in(96))

