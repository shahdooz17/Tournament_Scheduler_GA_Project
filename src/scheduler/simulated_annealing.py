import random
from scheduler.fitness import fitness

def measure_diversity(population):
    fitness_values = [fitness(ind) for ind in population]
    unique_fitness = len(set(fitness_values))
    if len(fitness_values) > 0:
        avg = sum(fitness_values) / len(fitness_values)
        variance = sum((x - avg) ** 2 for x in fitness_values) / len(fitness_values)
        std_dev = variance ** 0.5
    else:
        std_dev = 0
    return unique_fitness, std_dev

def local_search_refined(schedule, max_iterations=5):
    """Applies a simpler, less disruptive local search."""
    improved_schedule = schedule.copy()
    current_penalty = fitness(improved_schedule)

    for _ in range(max_iterations):

        if len(improved_schedule) > 1:
            idx1 = random.randint(0, len(improved_schedule) - 2)
            idx2 = idx1 + 1
            temp_schedule = improved_schedule.copy()
            temp_schedule[idx1], temp_schedule[idx2] = temp_schedule[idx2], temp_schedule[idx1]
            new_penalty = fitness(temp_schedule)

            if new_penalty < current_penalty:
                improved_schedule = temp_schedule
                current_penalty = new_penalty
            else:
                pass 

    return improved_schedule
