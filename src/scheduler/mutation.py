import random
from data import load_data as ld
teams = ld.load_teams()
venues = ld.load_venues()

def swap_mutation(schedule):
    mutated = schedule.copy()
    idx = random.randint(0, len(mutated) - 1)

    all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sunday"]
    all_times = ["01:00-03:00","03:00-05:00", "05:00-07:00", "07:00-09:00", "09:00-11:00"]

    new_day = random.choice(all_days)
    new_time = random.choice(all_times)
    new_venue = random.choice(venues)["name"]

    mutated[idx]["day"] = new_day
    mutated[idx]["time"] = new_time
    mutated[idx]["venue"] = new_venue

    return mutated