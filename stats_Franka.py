import streamlit as st
import pandas as pd

# Create sample DataFrame with game names and guesses

games_data = pd.DataFrame({
    "Historical Figure": ["Game 1", "Game 2", "Game 3", "Game 4", "Game 5"],
    "Guesses": [3, 4, 6, 2, 8]
})

# Variables we need 
average_guesses_current = games_data["Guesses"].mean()
average_guesses_updated = 3
delta = average_guesses_current - average_guesses_updated

number_of_rounds = len(games_data["Historical Figure"])


# Display the bar chart using st.bar_chart

st.title("How did you do?")

st.bar_chart(
    data=games_data,
    x="Historical Figure",
    y="Guesses",
    x_label="Historical Figure",
    y_label="Number of Guesses",
    use_container_width=True
)

# Display averages, total rounds, accuracy

col1, col2, col3 = st.columns(3)
col1.metric(label="Average Guesses per Game", value=f"{average_guesses_updated:.2f}", delta=delta, delta_color="inverse")
col2.metric(label="Total Rounds", value=number_of_rounds)
col3.metric("Accuracy", "86%", "4%")


