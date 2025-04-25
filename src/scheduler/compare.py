import pandas as pd
from scheduler.fitness import fitness

def compare_random_vs_optimized(random_schedule,optimized_schedule):
    random_penalty = fitness(random_schedule)
    optimized_penalty = fitness(optimized_schedule)

    random_schedule_data=[{
        "Team 1": match['team1'],
        "Team 2": match['team2'],
        "Day": match['day'],
        "Time": match['time'],
        "Venue": match['venue']

    }for match in random_schedule]

    optimized_schedule_data=[{
        "Team 1": match['team1'],
        "Team 2": match['team2'],
        "Day": match['day'],
        "Time": match['time'],
        "Venue": match['venue']

    }for match in optimized_schedule]

    random_schedule_df = pd.DataFrame(random_schedule_data)
    optimized_schedule_df = pd.DataFrame(optimized_schedule_data)

    comparison_result={
        "Random Schedule Penalty": random_penalty,
        "Optimized Schedule Penalty": optimized_penalty,
        "Improvement in Penalty": random_penalty - optimized_penalty,
        "Random Schedule Data": random_schedule_df,
        "Optimized Schedule Data": optimized_schedule_df
    }

    return comparison_result