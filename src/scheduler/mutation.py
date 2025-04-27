import random
from data import load_data as ld
teams = ld.load_teams()
venues = ld.load_venues()

def swap_mutation(schedule):
    mutated = schedule.copy()
    
    idx1 = random.randint(0, len(mutated) - 1)
    idx2 = random.randint(0, len(mutated) - 1)
    
    while idx1 == idx2:
        idx2 = random.randint(0, len(mutated) - 1)

    mutated[idx1]['day'], mutated[idx2]['day'] = mutated[idx2]['day'], mutated[idx1]['day']
    mutated[idx1]['time'], mutated[idx2]['time'] = mutated[idx2]['time'], mutated[idx1]['time']
    mutated[idx1]['venue'], mutated[idx2]['venue'] = mutated[idx2]['venue'], mutated[idx1]['venue']

    return mutated

def scramble_mutation(schedule):
    mutated = schedule.copy()
    size = len(mutated)

    if size < 2:
        return mutated

    start = random.randint(0, size - 2)
    end = random.randint(start + 1, size - 1)

    subset = mutated[start:end + 1]

    random.shuffle(subset)

    mutated[start:end + 1] = subset

    return mutated