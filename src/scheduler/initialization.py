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
    
    for _ in range(num_individuals):
        schedule = []
        venue_time_slots = set() 
        team_time_slots = set()   

        current_team_pairs = team_pairs.copy() 
        random.shuffle(current_team_pairs) 
        
        for team1, team2 in current_team_pairs:
            max_attempts = 100
            attempts = 0
            valid = False
            
            while not valid and attempts < max_attempts:
                venue = random.choice(venues)
                day, time = random.choice(timeslots)
                attempts += 1

                venue_conflict = (venue["name"], day, time) in venue_time_slots
                team1_conflict = (team1["name"], day, time) in team_time_slots
                team2_conflict = (team2["name"], day, time) in team_time_slots
                
                if not (venue_conflict or team1_conflict or team2_conflict):
                    match = {
                        "team1": team1["name"],
                        "team2": team2["name"],
                        "day": day,
                        "time": time,
                        "venue": venue["name"]
                    }

                    schedule.append(match)
                    venue_time_slots.add((venue["name"], day, time))
                    team_time_slots.add((team1["name"], day, time))
                    team_time_slots.add((team2["name"], day, time))
                    valid = True
            

        population.append(schedule)

    return population