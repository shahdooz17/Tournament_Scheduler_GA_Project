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

    safety_counter = 0
    max_safety = size * 2
    
    none_count = child.count(None)
    while none_count > 0 and safety_counter < max_safety:
        match = parent2[p2_idx]
        if match not in child:
            child[c_idx] = match
            none_count -= 1
        p2_idx = (p2_idx + 1) % len(parent2)
        c_idx = (c_idx + 1) % len(child)
        safety_counter += 1
    
    if none_count > 0:
        for i in range(len(child)):
            if child[i] is None:
                team_pairs = [(teams[i]["name"], teams[j]["name"]) for i in range(len(teams)) for j in range(i + 1, len(teams))]
                random.shuffle(team_pairs)
                
                for team1_name, team2_name in team_pairs:
                    if not any(m is not None and m["team1"] == team1_name and m["team2"] == team2_name for m in child):
                        venue = random.choice(venues)
                        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sunday"]
                        times = ["01:00-03:00", "03:00-05:00", "05:00-07:00", "07:00-09:00", "09:00-11:00"]
                        
                        child[i] = {
                            "team1": team1_name,
                            "team2": team2_name,
                            "day": random.choice(days),
                            "time": random.choice(times),
                            "venue": venue["name"]
                        }
                        break
    

    if None in child:
        from scheduler.initialization import initialization
        return initialization(1)[0]
    
    try:
        assert len(set(tuple(match.items()) for match in child)) == len(child), "Duplicated or missing matches in child"
    except (AssertionError, AttributeError):
        return parent1.copy()
    
    return child


def cyclic_crossover(parent1, parent2):
    size = len(parent1)
    child = [None] * size  

    if None in parent1 or None in parent2:
        return parent1.copy() if None not in parent1 else parent2.copy()

    try:
        visited = [False] * size  
        cycle = 0  

        while any(not visited[i] for i in range(size)): 
            current_idx = visited.index(False)
            indices_in_cycle = []  

            while not visited[current_idx]: 
                indices_in_cycle.append(current_idx)
                visited[current_idx] = True
                
                try:
                    current_idx = parent2.index(parent1[current_idx])
                except ValueError:
                    unvisited = [i for i, v in enumerate(visited) if not v]
                    current_idx = unvisited[0] if unvisited else -1
                    break

            if cycle % 2 == 0:
                for idx in indices_in_cycle:
                    child[idx] = parent1[idx]
            else:
                for idx in indices_in_cycle:
                    child[idx] = parent2[idx]

            cycle += 1

        if None in child:
            return parent1.copy()
            
        return child
        
    except Exception:
        return parent1.copy()
