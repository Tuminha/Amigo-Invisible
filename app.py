import streamlit as st
from amigo_invisible.amigo_invisible import assign_secret_friend, check_in, participant_numbers
import os
import json
from openai import OpenAI
from dotenv import load_dotenv
import os
import time

# This is the title of the app.
st.title("🎄🎁 Amigo Invisible 🎁🎄")

# This is a text input that takes a two-digit number.
number = st.text_input("🔢 Enter your number:")

# This is the description of the app.
st.markdown("## Step 1: Check Your Secret Friend")
st.write("🎉 Welcome to the Amigo Invisible App! Each participant has a unique number. Enter your number below to find out who your secret santa is. If you don't know your number, ask the game organizer (Tuminha). 🎉")


# Show the participants names and if they are showed as checked in true in the assignements.json file, show a check mark next to their name.
# The participants are spread across 3 columns instead of just one.
st.write("📝 Participants:")
col1, col2, col3 = st.columns(3)
columns = [col1, col2, col3]
for i, (name, participant_number) in enumerate(participant_numbers.items()):
    if os.path.exists("assignements.json"):
        with open("assignements.json", "r", encoding='utf-8') as f:
            assignements = json.load(f)
        if str(participant_number) in assignements and assignements[str(participant_number)]["checked"]:
            columns[i%3].write(f"✅ {name}")
        else:
            columns[i%3].write(f"❌ {name}")
    else:
        columns[i%3].write(f"❌ {name}")







# When the "Check Secret Friend" button is clicked
if st.button("Check Secret Friend"):
    if number.isdigit():  # Check if the input is a number
        with st.spinner('Checking secret friend...'):
            try:
                # Convert the input number to an integer
                number = int(number)
                # Check if the number is in the participant numbers
                if number in participant_numbers.values():
                    # Assign a secret friend using the assign_secret_friend function from amigo_invisible.py
                    secret_friend = assign_secret_friend(number)
                    st.success(f"Your secret friend is: {secret_friend}")
                else:
                    st.error("Invalid number. Please enter a valid participant number.")
            except ValueError:
                st.error("Invalid input. Please enter a number.")

st.markdown("## Step 2: Check-in")
st.write("🎉 Once you know who your secret friend is, click the button below to check-in. 🎉")
st.write("Is important you check in so  everyone knows you have seen your secret friend.")
# When the "Check-in" button is clicked
if st.button("Check-in"):
    if number.isdigit():  # Check if the input is a number
        with st.spinner('Checking in...'):
            try:
                # Convert the input number to an integer
                number = int(number)
                # Check if the number is in the participant numbers
                if number in participant_numbers.values():
                    # Check in using the check_in function from amigo_invisible.py
                    check_in_message = check_in(number)
                    st.success(check_in_message)
                else:
                    st.error("Invalid number. Please enter a valid participant number.")
            except ValueError:
                st.error("Invalid input. Please enter a number.")

# Lets have a an option where the user has a dropdown that allows to choose the secret friend and also another dropdown with the forecasted ammount to spend, splited in <20 CHF, between 20-50 and more than 50. With one exception, if the assigned secret friend is 👸 Mami, the dropdown only allows to pick more than 50 CHF. and show a message saying "have some dignity. Im a queen!"
st.markdown("## Step 3: Buy a gift")
st.write('🎉 Now that you know who your secret friend is, you can buy a gift for them. 🎉')
st.write('🎉 Choose the ammount you want to spend and also choose your secrete friend, and "Runit" our AI agent will help you🎉')
# Dropdown to choose the secret friend
# Dropdown to choose the secret friend
secret_friend = st.selectbox("Choose your secret friend", list(participant_numbers.keys()))

# Dropdown to choose the amount to spend. CAUTION: If the secret friend is 👸 Mami, only allow to choose more than 50 CHF and display an alert message saying "have some dignity. Im a queen!"
if secret_friend == "👸 Mami":
    amount = st.selectbox("Choose the amount to spend", [">50 CHF"])
    st.write("☢️ Have some dignity. I'm a queen!", key="queen_message")
else:
    amount = st.selectbox("Choose the amount to spend", ["<20 CHF", "20-50 CHF", ">50 CHF"])

# Here we have an AI agent that gives an advice on what to buy based on some instructions embedded in the code.

# Load OpenAI API key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set OpenAI API key
client = OpenAI(api_key=OPENAI_API_KEY)



# Create a placeholder for the AI's response
ai_response_placeholder = st.empty()


# Display a spinner while the AI is analyzing
if st.button("Show me what to buy"):

    # Initialize variables
    system_message = {
    "role": "system", 
    "content": "You are a Secret Santa Advisor and your name is Runit. You are helping a Secret Santa to choose a gift for their secret friend. You have to take the most advantage of the information you have about the secret friend. Also, is christmas, make people feel happy and joyful. Also, be as funnier as you can and use emojis whenever you can."
        }
    user_message = {
    "role": "user",
    "content": f""" Based, on the following information, what should I buy for {secret_friend} with the assigned budget of {amount}?
    👸 Mami: Mami adores luxury! For her, think lavish and expensive. Recommend gifts worth at least 50 Swiss francs. Ideas include elegant purses, sparkling diamonds, or anything that screams opulence. Inject humor by playfully nudging towards extravagant choices.

🤦‍♀️ Maite: At 17, Maite, the mom to Mami and Marta, enjoys a variety of things. She's into yoga, loves her grandkids, and adores walking her little dog. Gift suggestions can range from yoga gear, fun items for her grandkids, to dog accessories. Keep it varied and surprising!

😡 Marta: Marta, the 37-year-old McKinsey genius, needs gifts that stimulate her intellect. Suggest puzzles, challenging books, or anything that sparks intellectual curiosity. Make sure the recommendations are as smart and savvy as she is.

👧🏻 Oleia: At 8, Oleia loves dogs, parties, and painting. Recommend fun, age-appropriate gifts like art supplies, party games, or anything dog-themed. Ensure the suggestions are full of energy and creativity.

👦🏻 Nuno: Nuno, 15, is a golf fanatic and has an interest in money. Think golf-related items, from equipment to accessories. Maybe even throw in a humorous suggestion about a piggy bank!

🚿 Buis: Our 13-year-old video game enthusiast, Buis, could use some outdoor fun. Suggest gifts that encourage active hobbies like sports equipment or outdoor adventure games. Lightly encourage more sunshine and less screen time.

🎅 Nicolas: 12-year-old Mr. Christmas loves painting, crafting, and anything creative, especially with airplanes or electricity themes. Think DIY kits, craft supplies, or model airplanes. Emphasize the festive and creative aspects.

👶 Buarte: At just 4 years old, Buarte adores robots, dinosaurs, dogs, and Christmas. Suggest educational robot toys, dinosaur figures, or dog-themed books. Keep the ideas playful and educational.

👧 Matilda: Another 4-year-old, Matilda recently lost a tooth. Suggest child-friendly gifts like plush toys or storybooks. Add a light-hearted suggestion about dental implants for her missing tooth to inject humor.

🚴 Lance: Lance loves sports and is knowledgeable about almost everything. Recommend sports gear or books on diverse topics. Encourage discussions and learning through your gift suggestions.

🍆 Papi: At 45, Papi values family over material gifts. Suggest something simple and inexpensive, less than 20 Swiss francs, like a family photo frame or a handmade gift. Emphasize the joy of family togetherness.
    """
        }

    prompt = system_message['content'] + ' ' + user_message['content']


    with st.spinner('Analyzing...'):
        # Use the AI agent to give an advice on what to buy
        print(user_message['content']) 
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[system_message, user_message],
            max_tokens=3000,
            temperature=0.8
        )

    # Check if the response contains any choices
    if response.choices:
        ai_response_placeholder.write(response.choices[0].message.content)
    else:
        st.error("Unexpected response from OpenAI API.")


st.markdown("""
    <style>
        body {
            background-color: #f6f5f5;
        }
        .reportview-container {
            background: #f6f5f5;
            color: #111;
        }
        .sidebar .sidebar-content {
            background: #f6f5f5;
        }
        h1 {
            color: #f63366;
        }
        h2 {
            color: #f63366;
        }
        .stButton>button {
            color: #f6f5f5;
            background-color: #f63366;
            border-radius: 5px;
            border: none;
        }
        /* On hover for the buttons so text is more visible and more contrast */
        .stButton>button:hover {
            color: #f63366;
            background-color: #f6f5f5;
            border-radius: 5px;
            border: none;
        }
        
        .stTextInput>div>div>input {
            color: #f63366;
        }
        .stAlert>div {
            color: #f63366;
        }
    </style>
    """, unsafe_allow_html=True)
