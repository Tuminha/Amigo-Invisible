Table of contents



## Amigo Invisible (Secret Santa) App Overview

The Amigo Invisible, or Secret Santa, is an innovative app designed to add fun and simplicity to the traditional Secret Santa game. The core purpose of this app is to facilitate families, friends, or colleagues in randomly assigning a 'secret friend' or 'secret Santa' to each participant in an unbiased and exciting manner.

## How the App Works

### Random Assignment
Utilizing a Python-based backend, the app intelligently shuffles a list of participants and randomly assigns each person a 'secret Santa'.

### Participant Anonymity
Each participant is assigned a unique secret number to maintain confidentiality.

### Streamlit Frontend
To enhance user experience, the app boasts a user-friendly frontend developed with Streamlit. Participants can simply input their secret number on this interface to discover who their secret Santa is.

### Gift Giving Made Easy
The overarching goal is to ensure every participant is assigned someone who will thoughtfully select and give a present, making the gift exchange process seamless and enjoyable.

This app is more than just a tool; it's a digital facilitator of joy and surprise, making your Secret Santa event hassle-free and memorable.

## Features of the Amigo Invisible (Secret Santa) App

The Amigo Invisible app is designed with user engagement and convenience in mind, offering a suite of features that enhance the Secret Santa experience. These features are categorized into three primary sections:

### Secret Number Assignment:

Each participant is assigned a unique secret number by the administrator of the game.
This number is confidentially communicated from the administrator to the participant.
Participants enter their secret number into the app to reveal their assigned Secret Santa. This process ensures anonymity and adds an element of surprise to the gift exchange.

### Check-In Functionality:

The app includes a 'Check-In' feature, which allows participants to confirm their participation and assignment.
Once a participant checks in, the information is updated in the app's frontend. This feature provides transparency, enabling other participants to see who has already been assigned a secret friend.

### AI-Powered Gift Recommendations:

A standout feature of the app is its integration with an AI-powered recommendation system.
By leveraging OpenAI's language models through an API, the app offers personalized gift suggestions.
Participants simply input their budget, and the AI suggests suitable gifts for their secret friend. This innovative feature takes the guesswork out of gift selection, ensuring thoughtful and appropriate presents within the set budget.

These carefully crafted features make the Amigo Invisible app not just a tool for organizing Secret Santa events but a comprehensive platform that enhances the entire experience, from assignment to gift selection, fostering a joyful and memorable holiday tradition.

## Technologies Used

The Amigo Invisible app is built using a variety of technologies, libraries, and tools that together create a seamless and user-friendly experience. Below is an overview of the key technologies utilized:

### Python

Python: The core language used for the backend development of the app, known for its simplicity and readability.
JSON: Utilized for data storage and manipulation, particularly for managing participant assignments.
OS Module: Integrated for interacting with the operating system, such as checking for the existence of files.
Random Module: Employed to ensure the randomness in the assignment of Secret Santas, crucial for the fairness of the game.

### Streamlit

Streamlit: An innovative framework for building interactive and intuitive web applications entirely in Python. Used for creating the frontend of the app, offering participants a user-friendly interface to interact with.

### OpenAI's GPT-4 API

OpenAI's GPT-4 API: Leveraged for integrating advanced AI capabilities into the app. The API is used to provide AI-powered gift recommendations, enhancing the user experience by suggesting creative and thoughtful gift ideas.

### Additional Libraries and Tools

Dotenv: For managing environment variables, ensuring sensitive information such as API keys are securely handled.
OpenAI Python Client: A Python library provided by OpenAI for easy integration of their language models into applications.

### Development Tools

Git: Used for version control, allowing for effective tracking and management of code changes.
GitHub: Hosts the code repository and facilitates version control and collaboration.
Visual Studio Code: The chosen Integrated Development Environment (IDE) for writing and editing the code, known for its robust features and support for Python development.

## Existing Features
### Welcome Screen
**Initial Interaction:** Upon launching the app, users are greeted with a welcoming interface.
**Participant Number Entry:** Participants are prompted to enter their unique secret number to proceed.
![Welcome Screen](images/App_home_screen_1.png)
### Main Menu
**Secret Friend Reveal:** After entering a valid number, participants can discover their secret Santa.
**Instructions and Rules:** Clear guidelines are provided on how to participate and engage with the app.
![Main Menu](images/enter_the_number.png)
### Participant Assignment and Check-In
**Random Secret Santa Assignment:** The app assigns a secret Santa to each participant in a random and fair manner.
**Check-In Functionality:** Participants can check in, and the app updates this status for all users to see.
**Transparency and Engagement:** The app promotes a transparent process where everyone knows who has checked in.
**Real-Time Updates:** After the check-in, the list of users that have already checked in is updated and visible to everyone. However, the page needs to be refreshed to see the updated list.
![Participant Assignment and Check-In](images/check_in.png)
![Updated Participants List](images/participants_update.png)
### AI-Powered Gift Recommendations
**Interactive Gift Suggestion:** Participants can use the OpenAI-powered feature to get gift suggestions.
**Personalized Experience:** By inputting their budget and the assigned secret friend, users receive customized gift ideas.
**Enhanced User Experience:** This feature adds a layer of innovation and fun to the gift selection process.
![AI-Powered Gift Recommendations](images/AI_gift_recommendation.png)
### Responsive Web Interface
**Streamlit Framework:** The app's frontend, built with Streamlit, offers a responsive and intuitive user interface.
**Cross-Platform Accessibility:** Accessible on various devices, ensuring a wide reach among users.
![Responsive Web Interface](images/iphone_app.png)
### Administrative Features
**Game Reset Option:** Administrators can reset the game, including reassigning secret Santas, using a secure password.
![Game Reset Option](images/game_reset.png)

**Data Management:** Efficient handling of participant data and assignments through JSON file manipulation.
**Environment Variables:** Secure management of API keys and sensitive data using the dotenv library.
{Placeholder for image: Administrative Features}
## Features Left to Implement
**Multilingual Support:** To cater to a diverse user base by providing multiple language options.
**Enhanced Customization:** Allowing users to add personal touches, like custom messages to their secret friends.
**Participant Dashboard:** A feature for participants to view past games, their gift history, and more.
**Mobile App Version:** Expanding the platform to a dedicated mobile application for increased accessibility.

## Testing

### General Testing
The Amigo Invisible app underwent rigorous testing to ensure functionality, usability, and reliability. Testing was conducted across various aspects of the application, including code quality, user interaction, and AI integration.

### Development and Deployment Environment
The app was developed and tested in a robust development environment, ensuring consistent performance across different platforms. Additionally, the app was deployed and tested to confirm its functionality in a live setting.

### PEP8 Compliance
Code quality was a priority, and as such, all Python files (amigo_invisible.py, app.py) were checked for PEP 8 compliance using the Code Institute's PEP8 online tool. The results indicated 100% compliance, with no errors found across all files.

![PEP8 Test Results for amigo_invisible.py](images/Amigo_invisible_validation.png)
![PEP8 Test Results for app.py](images/App.py_error_check.png)

### Automated Testing
Automated tests were written and run using Python's unittest framework, ensuring that all core functionalities of the application were working as expected. The test.py file contains a suite of tests that cover various scenarios, including participant assignment, secret friend revelation, and error handling. All tests were executed successfully, confirming the robustness of the application logic.

![Automated Test Results](images/test_amigo_invisible.png)

### User Stories Testing
Testing was also aligned with user stories to ensure that the app met the needs and expectations of its users. Each user story was methodically tested to verify that the app provided the intended experience and functionality.

#### Participant Number Entry:
* Action: Participants enter their secret number.
* Expected Result: The app reveals the assigned secret Santa.
* Actual Result: Worked as expected.

![Participant Number Entry](images/Check_secret_friend.png)

#### Check-In Functionality:
* Action: Participants use the check-in feature.
* Expected Result: The app updates the check-in status.
* Actual Result: Worked as expected.

![Check-In Functionality](images/check_in.png)

#### AI-Powered Gift Recommendations:
* Action: Users input their budget and get gift suggestions.
* Expected Result: The app provides relevant gift recommendations.
* Actual Result: Worked as expected, with AI suggestions aligning with user inputs.

![AI-Powered Gift Recommendations](images/gift_recommendations_1.png)

#### Game Reset by Admin:
* Action: Admin enters the reset password and resets the game.
* Expected Result: The game resets and reassigns secret Santas.
* Actual Result: Functioned correctly, allowing for a fresh start of the game.

![Game Reset Feature](images/game_reset.png)
