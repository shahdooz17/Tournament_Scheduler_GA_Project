import random
from scheduler.initialization import initialization
from scheduler.fitness import fitness
from scheduler.crossover import order_crossover, cyclic_crossover
from scheduler.mutation import swap_mutation, scramble_mutation
from scheduler.selection import tournament_selection
from scheduler.survivor import elitism

def genetic_algorithm(
    population_size,
    generations,
    crossover_method,
    mutation_method,
    mutation_probability=0.1,
    crossover_probability=0.9,
    tournament_size=2,
    top_n_elitism=1,
    initial_population=None  # <-- new!
):
    if initial_population is not None:
        population = initial_population
    else:
        population = initialization(population_size)
    penalties_per_generation = []

    for generation in range(generations):
        penalties = [fitness(schedule) for schedule in population]
        penalties_per_generation.append(min(penalties))

        sorted_population = [x for _, x in sorted(zip(penalties, population), key=lambda pair: pair[0])]
        elite_individuals = elitism(sorted_population, top_n=top_n_elitism)

        selected_parents = tournament_selection(population, tournament_size=tournament_size)

        offspring = []
        for i in range(0, len(selected_parents), 2):
            if i + 1 < len(selected_parents):
                parent1, parent2 = selected_parents[i], selected_parents[i + 1]
                if random.random() < crossover_probability:
                    child1 = crossover_method(parent1, parent2)
                    child2 = crossover_method(parent2, parent1)
                    offspring.extend([child1, child2])
                else:
                    offspring.extend([parent1, parent2])

        mutated_offspring = []
        for child in offspring:
            if random.random() < mutation_probability:
                mutated_offspring.append(mutation_method(child))
            else:
                mutated_offspring.append(child)

        population = elite_individuals + mutated_offspring
        population = population[:population_size]

    final_sorted_population = sorted(population, key=fitness)
    return final_sorted_population, penalties_per_generation
