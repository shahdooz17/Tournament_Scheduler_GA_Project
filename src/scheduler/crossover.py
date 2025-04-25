import random
from data import load_data as ld

teams = ld.load_teams()
venues = ld.load_venues()

def order_crossover(parent1, parent2):
    size = len(parent1)
    start , end =sorted(random.sample(range(len(parent1)), 2))

    child = [None] * size
    child[start:end +1] = parent1[start:end+1]

    p2_idx = (end+1 ) % len(parent2)
    c_idx = (end+1 ) % len(child)

    while None in child :
        match = parent2[p2_idx]
        if match not in child :
            child[c_idx] = match 
            c_idx = (c_idx+1) % len(child)

        p2_idx = (p2_idx+1 ) % len(child)


    assert len(set(tuple(match.items()) for match in child )) == len(child) , "Duplicated or missing matches in child"   

    ##existing_pairs = {(m['team1'], m['team2']) for m in child[start:end]}

    # Fill remaining genes based on match pairing only
    ##idx = end
    ##for match in parent2:
    ##    pair = (match['team1'], match['team2'])
    ##    if pair not in existing_pairs:
    ##        if idx >= size:
    ##            idx = 0
    ##        child[idx] = {
    ##            "team1": match["team1"],
    ##            "team2": match["team2"],
    ##            "day": match["day"],     # temporary
    ##            "time": match["time"],   # temporary
    ##            "venue": match["venue"]  # temporary
    ##        }
    ##        existing_pairs.add(pair)
    ##       idx += 1

    # Re-randomize time/venue for feasibility (you can do better with repair later)
    ##all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sunday"]
    ##all_times = ["01:00-03:00","03:00-05:00", "05:00-07:00", "07:00-09:00", "09:00-11:00"]
    ##for match in child:
    ##    venue = random.choice(venues)
    ##    match["day"] = random.choice(all_days)
    ##    match["time"] = random.choice(all_times)
    ##    match["venue"] = venue["name"]

    return child