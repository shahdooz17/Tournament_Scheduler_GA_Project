import pandas as pd
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def load_teams():
    path = os.path.join(CURRENT_DIR, "Football Stadiums.csv")
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df = df[df['Country'] == "England"]
    return [{"id": i + 1, "name": row["HomeTeams"]} for i, row in df.iterrows()]

def load_venues():
    path = os.path.join(CURRENT_DIR, "Football Stadiums.csv")
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df = df[df['Country'] == "England"]
    return [{"id": f"V{i + 1}", "name": row["Stadium"]} for i, row in df.iterrows()]
