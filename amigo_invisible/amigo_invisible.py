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
# It also has to check if the assignments.json file exists and if it does, it has to create it the first time it is executed.
# The file should contain key values with the name, secret friend assigned and also a boolean to register that this person already checked in and already knows his her secret friend.
# The function should return the secret friend assigned and write it into the assignments.json file.
# Handling errors and also the case when the number entered is not in the list of participants should be considered, avoiding overwriting the file.
# The function should also return a message to the user with the name of the secret friend assigned.
# Save results in a file called assignments.json



def assign_secret_friend():
    """
    Randomly assign a secret friend to each participant.
    """
    shuffled_participants = participants[:]
    random.shuffle(shuffled_participants)

    assignments = {}
    for i, participant in enumerate(participants):
        if participant == shuffled_participants[i]:
            # In rare cases, a participant might end up with themselves after shuffling,
            # perform a simple swap to fix it.
            swap_index = (i + 1) % len(participants)
            shuffled_participants[i], shuffled_participants[swap_index] = shuffled_participants[swap_index], shuffled_participants[i]

        assignments[participant_numbers[participant]] = {"secret_friend": shuffled_participants[i], "checked": False}

    # Write to the assignments file
    with open("assignments.json", "w", encoding='utf-8') as f:
        json.dump(assignments, f)

    return assignments

# Run the function to assign secret friends
assigned_friends = assign_secret_friend()

    
def check_in(number):
    """
    This function checks in a participant.
    It takes a number as input, checks if the number is in the list of participants,
    and if it is, it checks in the participant.
    The function also checks if the assignments.json file exists and if it does not,
    it returns an error message. If the file exists, it reads it and checks if the number is in the assignments.
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
    if not os.path.exists("assignments.json"):
        return "The assignments file does not exist"

    # If it exists, open it and read it
    try:
        with open("assignments.json", "r", encoding='utf-8') as f:
            assignments = json.load(f)
    except Exception as e:
        return "Error reading assignments file: " + str(e)

    # Check if the number is in the assignments
    if number not in assignments:
        return "The participant has not been assigned a secret friend"

    # If the participant has already checked in, return a message
    if "checked" in assignments[number] and assignments[number]["checked"]:
        return "The participant that is number {} that corresponds to participant {} has already checked in and knows the secret friend that is {}".format(number, [name for name, num in participant_numbers.items() if num == int(number)][0], assignments[number]["secret_friend"])

    # If the participant has not checked in, update the checked status to true
    assignments[number]["checked"] = True

    # Write the updated data back to the file
    try:
        with open("assignments.json", "w", encoding='utf-8') as f:
            json.dump(assignments, f)
    except Exception as e:
        return "Error writing to assignments file: " + str(e)

# Return a message to the user with the name of the secret friend assigned
    participant_name = [name for name, num in participant_numbers.items() if num == int(number)][0]
    return "Check-in successful for participant number {}, that corresponds to {} and their secret friend is {}".format(number, participant_name, assignments[number]["secret_friend"])



# Do one iteration to check that everything works fine and we can print the particiapnt and its assigned friend

# Assign secret friends
assigned_friends = assign_secret_friend()

# Check-in each participant and print the result
for number in participant_numbers.values():
    print(check_in(number))




