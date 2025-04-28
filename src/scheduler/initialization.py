import random
from data import load_data as ld

teams = ld.load_teams()
venues = ld.load_venues()

def initialization(num_individuals):
    timeslots = [
        (day, time) for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sunday"]
        for time in ["01:00-03:00","03:00-05:00", "05:00-07:00", "07:00-09:00", "09:00-11:00"]
    ]
    population = []
    team_pairs = [(teams[i], teams[j]) for i in range(len(teams)) for j in range(i + 1, len(teams))]
    random.shuffle(team_pairs)
    
    for _ in range(num_individuals):
        schedule = []

        for team1, team2 in team_pairs:
            max_attempts = 100
            attempts = 0
            valid = False
            
            while not valid and attempts < max_attempts:
                venue = random.choice(venues)
                day, time = random.choice(timeslots)
                attempts += 1

                match = {
                    "team1": team1["name"],
                    "team2": team2["name"],
                    "day": day,
                    "time": time,
                    "venue": venue["name"]
                }

                schedule.append(match)

                valid = True

        population.append(schedule)

    return population