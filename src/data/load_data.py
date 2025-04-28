import pandas as pd
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(CURRENT_DIR, "Football Stadiums.csv")
ENCODING = 'latin1'

def load_data():
    df = pd.read_csv(FILE_PATH, encoding=ENCODING, low_memory=False)
    df = df[df["Country"] == "South Korea"]
    return df

def load_teams():
    df = load_data()
    return [{"id": i + 1, "name": row["HomeTeams"]} for i, row in df.iterrows()]

def load_venues():
    df = load_data()
    return [{"id": f"V{i + 1}", "name": row["Stadium"]} for i, row in df.iterrows()]