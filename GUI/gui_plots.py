import streamlit as st
import pandas as pd
from src.scheduler.fitness import fitness

def display_schedule(schedule, idx, title="Schedule"):
    penalty = fitness(schedule)
    schedule_data = [{
        "Team 1": match['team1'],
        "Team 2": match['team2'],
        "Day": match['day'],
        "Time": match['time'],
        "Venue": match['venue']
    } for match in schedule]

    schedule_df = pd.DataFrame(schedule_data)
    st.subheader(f"{title} {idx + 1}")
    st.dataframe(schedule_df)
    st.write(f"Penalty: {penalty}")
