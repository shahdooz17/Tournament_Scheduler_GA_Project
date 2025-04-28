import random
from data import load_data as ld

teams = ld.load_teams()
venues = ld.load_venues()

def order_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(len(parent1)), 2))

    child = [None] * size
    child[start:end + 1] = parent1[start:end + 1]

    p2_idx = (end + 1) % len(parent2)
    c_idx = (end + 1) % len(child)

    none_count = child.count(None)
    while none_count > 0:
        match = parent2[p2_idx]
        if match not in child:
            child[c_idx] = match
            none_count -= 1
        p2_idx = (p2_idx + 1) % len(parent2)
        c_idx = (c_idx + 1) % len(child)

    assert len(set(tuple(match.items()) for match in child)) == len(child), "Duplicated or missing matches in child"
    
    return child


def cyclic_crossover(parent1, parent2):
    size = len(parent1)
    child = [None] * size  

    visited = [False] * size  
    cycle = 0  

    while any(not visited[i] for i in range(size)): 
        current_idx = visited.index(False)

        indices_in_cycle = []  

        while not visited[current_idx]: 
            indices_in_cycle.append(current_idx)
            visited[current_idx] = True

            current_idx = parent2.index(parent1[current_idx])

        if cycle % 2 == 0:
            for idx in indices_in_cycle:
                child[idx] = parent1[idx]
        else:
            for idx in indices_in_cycle:
                child[idx] = parent2[idx]

        cycle += 1

    return child

