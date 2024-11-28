import streamlit as st
import pandas as pd

# Data frame format we need 

#Intialise before first input beginning of new round
#Update on every single guess for current round

games_data = pd.DataFrame({
    "City_Given-Target_City": ["Tokio-Berlin", "Game 2", "Game 3", "Game 4", "Game 5"],
    "Guesses": [3, 4, 6, 2, 8]
})

# Variables we need

#Update every guess
average_guesses_current = games_data["Guesses"].mean()
average_guesses_previous = games_data["Guesses"].mean()
delta = average_guesses_current - average_guesses_previous 

#update every time a round is complete 
number_of_rounds = len(games_data["City_Given-Target_City"])

#update on every guess
number_of_non_capitals_current = 32
number_of_non_capitals_previous = 12

#update on every guess
#distance_target_named = CHATGPT 
#how_far_off = [200, 500, 1000, 2]
#average_far_off = mean (how_far_off)

#Update upon completon on every round
# Display the bar chart using st.bar_chart

st.title("How did you do? Let's review your stats.")

st.bar_chart(
    data=games_data,
    x="City_Given-Target_City",
    y="Guesses",
    x_label="Cities",
    y_label="Number of Guesses",
    use_container_width=True
)

#Update on every single round
# Display averages, total rounds, accuracy

col1, col2 = st.columns(2)
col1.metric(label="Average Guesses per Game", value=f"{average_guesses_current:.2f}", delta=delta, delta_color="inverse")
col2.metric(label="Total Rounds", value=number_of_rounds)


col1, col2 = st.columns(2)
col1.metric("On average, how far off were your guesses?", "8600km", "400km",delta_color="inverse")
col2.metric("How many non-capitals did you name?", number_of_non_capitals_current, number_of_non_capitals_previous, delta_color = "inverse")