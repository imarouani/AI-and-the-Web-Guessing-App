import streamlit as st
import random
import json
from difflib import SequenceMatcher

# Load people data from JSON file
def load_people():
    with open("assets/people.json", "r") as file:
        return json.load(file)

# Load the data once
people = load_people()

# Helper function to get a random person
def get_random_person(people_list):
    return random.choice(people_list)

# Function to calculate the difference in characters between two strings
def calculate_character_difference(guess, actual):
    sm = SequenceMatcher(None, guess.lower(), actual.lower())
    matches = sum(triple.size for triple in sm.get_matching_blocks())
    return abs(len(actual) - matches)

# Initialize session state
if 'goal' not in st.session_state:
    st.session_state.goal = get_random_person(people)
    st.session_state.hint_index = 0  # Start with the first hint

# Get the current goal and hint
current_person = st.session_state.goal
current_hint_index = st.session_state.hint_index
current_hint = current_person["hints"][current_hint_index]

# Display the hint
st.write("Hint:", current_hint)

# Get user's guess
guess = st.text_input(label="Who am I?")
st.write(current_person["name"])

# Check the guess
if guess:
    correct_name = current_person["name"]
    
    # Partial match check
    if guess.strip().lower() in correct_name.lower() or correct_name.lower() in guess.strip().lower():
        st.balloons()
        st.success(f"Correct! The answer was: {correct_name}")
        # Load a new goal and reset hints
        stsession_state.goal = get_random_person(people)
        st.session_state.hint_index = 0  # Reset hint index for new person
    else:
        # Calculate how many characters off the guess is
        char_diff = calculate_character_difference(guess.strip(), correct_name)
        remaining_guesses = len(current_person["hints"]) - current_hint_index - 1
        
        ###if char_diff <= 2:
        ###    st.warning(f"You're very close! Your guess is {char_diff} characters off.")
        ###else:
        ###    st.warning("Incorrect! Try again.")
        
        # Display number of guesses left
        if remaining_guesses > 0:
            st.info(f"You have {remaining_guesses} guesses left.")
        else:
            st.info(f"No guesses left! The correct answer was: {current_person['name']}")
            st.session_state.goal = get_random_person(people)
            st.session_state.hint_index = 0  # Reset hint index for new person

        # Move to the next hint if available
        if st.session_state.hint_index < len(current_person["hints"]) - 1:
            st.session_state.hint_index += 1
