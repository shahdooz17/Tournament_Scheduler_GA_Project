import random
from scheduler.fitness import fitness
def tournament_selection(population, tournament_size):

    tournament_size = min(tournament_size, len(population))

    selected_parents = []
    while len(selected_parents) < len(population) // 2:
        tournament_pool = random.sample(population, tournament_size)
        selected_parents.append(min(tournament_pool, key=lambda ind: fitness(ind)))
    
    return selected_parents