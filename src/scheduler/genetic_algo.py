import random
import streamlit as st
from scheduler.initialization import initialization
from scheduler.fitness import fitness
from scheduler.crossover import order_crossover, cyclic_crossover
from scheduler.mutation import swap_mutation, scramble_mutation
from scheduler.selection import tournament_selection
from scheduler.survivor import elitism

# Constants
POPULATION_SIZE = 30
MAX_GENERATIONS = 200
MUTATION_PROBABILITY = 0.1
TOURNAMENT_SIZE = 2
TOP_N_ELITISM = 1

def genetic_algorithm(population_size=POPULATION_SIZE, generations=MAX_GENERATIONS):
    population = initialization(population_size)
    penalties_per_generation = []

    for generation in range(generations):
        if generation % 10 == 0:
            st.text(f"Generation {generation + 1}")

        penalties = [fitness(schedule) for schedule in population]
        penalties_per_generation.append(min(penalties))

        sorted_population = [x for _, x in sorted(zip(penalties, population), key=lambda pair: pair[0])]
        elite_individuals = elitism(sorted_population, top_n=TOP_N_ELITISM)
        selected_parents = tournament_selection(population, tournament_size=TOURNAMENT_SIZE)

        offspring = []
        for i in range(0, len(selected_parents), 2):
            if i + 1 < len(selected_parents):
                parent1, parent2 = selected_parents[i], selected_parents[i + 1]

                crossover_method = random.choice([order_crossover, cyclic_crossover])
                child1 = crossover_method(parent1, parent2)
                if isinstance(child1, tuple) or (isinstance(child1, list) and isinstance(child1[0], list)):
                    child1 = child1[0]

                crossover_method = random.choice([order_crossover, cyclic_crossover])
                child2 = crossover_method(parent2, parent1)
                if isinstance(child2, tuple) or (isinstance(child2, list) and isinstance(child2[0], list)):
                    child2 = child2[0]

                offspring.extend([child1, child2])
            else:
                offspring.append(selected_parents[i])


        mutated_offspring = []
        for child in offspring:
            if random.random() < MUTATION_PROBABILITY:
                # 🔥 Randomly choose mutation method
                mutation_method = random.choice([swap_mutation, scramble_mutation])
                mutated_offspring.append(mutation_method(child))
            else:
                mutated_offspring.append(child)

        population = elite_individuals + mutated_offspring
        population = population[:population_size]

    sorted_population = sorted(population, key=fitness)

    while len(sorted_population) < population_size:
        sorted_population.append(random.choice(sorted_population))

    return sorted_population[:population_size], penalties_per_generation