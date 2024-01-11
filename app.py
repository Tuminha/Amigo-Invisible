import streamlit as st
from amigo_invisible.amigo_invisible import (
    assign_secret_friend, check_in, participant_numbers
)
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Assign secret friends at the start (if not already done)
if not os.path.exists("assignments.json"):
    assign_secret_friend()

# Streamlit app code
st.title("🎄🎁 Amigo Invisible 🎁🎄")
number = st.text_input("🔢 Enter your number:")
st.markdown("## Step 1: Check Your Secret Friend")
st.write("🎉 Welcome to the Amigo Invisible App! Enter your number below "
         "to find out who your secret santa is.")

# Show the participants names and their check-in status
st.write("📝 Participants:")
col1, col2, col3 = st.columns(3)
columns = [col1, col2, col3]

with open("assignments.json", "r", encoding='utf-8') as f:
    assignments = json.load(f)

for i, (name, participant_number) in enumerate(participant_numbers.items()):
    checked_in = assignments[str(participant_number)]["checked"]
    columns[i % 3].write(f"{'✅' if checked_in else '❌'} {name}")

# Check Secret Friend
if st.button("Check Secret Friend"):
    try:
        number = int(number)
        if number in participant_numbers.values():
            secret_friend_name = assignments[str(number)]["secret_friend"]
            st.success(f"Your secret friend is: {secret_friend_name}")
        else:
            st.error("Invalid number. Enter a valid participant number.")
    except ValueError:
        st.error("Invalid input. Please enter a number.")

# Check-in
st.markdown("## Step 2: Check-in")
if st.button("Check-in"):
    try:
        number = int(number)
        if number in participant_numbers.values():
            check_in_message = check_in(number)
            st.success(check_in_message)
            # Add a check mark of check in to the user that just checked in
            with open("assignments.json", "r", encoding='utf-8') as f:
                assignments = json.load(f)
            assignments[str(number)]["checked"] = True
            with open("assignments.json", "w", encoding='utf-8') as f:
                json.dump(assignments, f, ensure_ascii=False, indent=4)
        else:
            st.error("Invalid number. Enter a valid participant number.")
    except ValueError:
        st.error("Invalid input. Please enter a number.")

# Dropdown options for gift buying
st.markdown("## Step 3: Buy a gift")
st.write('🎉 Now that you know who your secret friend is, you can buy a gift'
         ' for them. 🎉')
st.write('🎉 Choose the amount you want to spend and also choose your secret'
         ' friend, and "Runit" our AI agent will help you🎉')

# Dropdown to choose the secret friend
secret_friend = st.selectbox("Choose your secret friend",
                             list(participant_numbers.keys()))

# Dropdown to choose the amount to spend
if secret_friend == "👸 Mami":
    amount = st.selectbox("Choose the amount to spend", [">50 CHF"])
    st.write("☢️ Have some dignity. I'm a queen!", key="queen_message")
else:
    amount = st.selectbox("Choose the amount to spend",
                          ["<20 CHF", "20-50 CHF", ">50 CHF"])

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
        "content": ("You are a Secret Santa Advisor and your name is Runit. "
                    "You are helping a Secret Santa to choose a gift for their"
                    " secret friend. Take advantage of the information you"
                    " have about the secret friend. Make people feel happy"
                    " and joyful this Christmas, and be as funny as you can"
                    " with emojis.")
    }
    user_message = {
        "role": "user",
        "content": (
            f"Based on the following information, what should I buy for "
            f"{secret_friend} with the assigned budget of {amount}?\n"
            "👸 Mami: Mami adores luxury! For her, think lavish and expensive. "
            "Recommend gifts worth at least 50 Swiss francs. Ideas include "
            "elegant purses, diamonds, or anything that screams opulence. "
            "Inject humor by nudging towards extravagant choices.\n"
            "🤦‍♀️ Maite: At 17, Maite, the mom to Mami and Marta, enjoys a"
            " variety of things. She's into yoga, loves her grandkids, "
            "and adores walking her dog. "
            "Gift suggestions can range from yoga gear, fun items for her "
            "grandkids, "
            "to dog accessories. Keep it varied and surprising!\n"
            "😡 Marta: Marta, the 37-year-old McKinsey genius, needs gifts "
            "that stimulate her intellect. "
            "Suggest puzzles, challenging books, or anything that sparks"
            " intellectual curiosity. Ensure recommendations are as smart"
            " and savvy as she is.\n"
            "👧🏻 Oleia: At 8, Oleia loves dogs, parties, and painting."
            " Recommend fun, age-appropriate gifts like art supplies,"
            " party games, or anything dog-themed. Ensure suggestions are"
            " full of energy and creativity.\n"
            "👦🏻 Nuno: Nuno, 15, is a golf fanatic and interested in money."
            " Suggest golf-related items, from equipment to accessories."
            " Maybe even a humorous suggestion about a piggy bank!\n"
            "🚿 Buis: Our 13-year-old video game enthusiast, Buis, could"
            " use some outdoor fun. Suggest gifts that encourage active"
            " hobbies like sports equipment or outdoor adventure games."
            " Encourage more sunshine and less screen time.\n"
            "🎅 Nicolas: 12-year-old Mr. Christmas loves painting,"
            " crafting, and anything creative, especially with airplanes"
            " or electricity themes. Suggest DIY kits, craft supplies,"
            " or model airplanes. Emphasize the festive and creative"
            " aspects.\n"
            "👶 Buarte: At just 4 years old, Buarte adores robots,"
            " dinosaurs, dogs, and Christmas. Suggest educational robot toys,"
            " dinosaur figures, or dog-themed books. Keep ideas playful"
            " and educational.\n"
            "👧 Matilda: Another 4-year-old, Matilda recently lost a tooth."
            " Suggest child-friendly gifts like plush toys or storybooks."
            " Add a light-hearted suggestion about dental implants for her"
            " missing tooth to inject humor.\n"
            "🚴 Lance: Lance loves sports and is knowledgeable about"
            " almost everything. Recommend sports gear or books on diverse"
            " topics. Encourage discussions and learning through your gift"
            " suggestions.\n"
            "🍆 Papi: At 45, Papi values family over material gifts."
            " Suggest something simple and inexpensive, less than 20 Swiss"
            " francs, like a family photo frame or a handmade gift."
            " Emphasize the joy of family togetherness."
        )
    }

    prompt = system_message['content'] + ' ' + user_message['content']

    with st.spinner('Analyzing...'):
        # Use the AI agent to give an advice on what to buy
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

# Add a button to reset the json file to restart the game
# It should only be used by the admin that knows the code to reset the game
# That is "132127"
password = st.text_input(
    "Enter the password to reset the game:", type="password"
    )
if st.button("Reset Game"):
    if password == "132127":
        # Delete the assignments.json file
        if os.path.exists("assignments.json"):
            os.remove("assignments.json")
        # Recreate the assignments.json file by calling assign_secret_friend
        assign_secret_friend()
        st.success("Game has been reset.")
    else:
        st.error("Incorrect password. Please try again.")

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

        /* On hover for buttons, text is more visible, more contrast */
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
