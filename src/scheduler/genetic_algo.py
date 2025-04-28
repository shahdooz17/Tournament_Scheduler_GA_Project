import random
import math
from scheduler.initialization import initialization
from scheduler.fitness import fitness
from scheduler.selection import tournament_selection
from scheduler.survivor import elitism
from scheduler.simulated_annealing import local_search_refined
from scheduler.simulated_annealing import measure_diversity

def genetic_algorithm(
    population_size,
    generations,
    crossover_method,
    mutation_method,
    initial_mutation_rate=0.1,
    crossover_probability=0.9,
    tournament_size=3,
    top_n_elitism=2,
    initial_population=None,
    stagnation_limit=75, 
    initial_temperature=50.0, 
    cooling_rate=0.995,
    local_search_frequency=25 
):
    if initial_population is not None:
        population = initial_population
    else:
        population = initialization(population_size)
        
    penalties_per_generation = []
    mutation_rate = initial_mutation_rate
    temperature = initial_temperature
    
    best_solution_ever = None
    best_penalty_ever = float("inf")
    generations_without_improvement = 0

    for generation in range(generations):
        penalties = [fitness(schedule) for schedule in population]
        
        current_best_penalty = min(penalties)
        current_best_idx = penalties.index(current_best_penalty)
        current_best_solution = population[current_best_idx]
        worst_penalty = max(penalties)
        
        previous_best_penalty_ever = best_penalty_ever
        if current_best_penalty < best_penalty_ever:
            best_penalty_ever = current_best_penalty
            best_solution_ever = current_best_solution.copy()
            generations_without_improvement = 0
        else:
            generations_without_improvement += 1
            
        penalties_per_generation.append(best_penalty_ever)
        
        print(f"Generation {generation}: Best penalty = {current_best_penalty}, Worst penalty = {worst_penalty}, Best Ever = {best_penalty_ever}, Stagnation: {generations_without_improvement}")
        
        unique_fitness, std_dev = measure_diversity(population)
        print(f"Generation {generation}: Diversity metrics - Unique fitness values: {unique_fitness}, StdDev: {std_dev:.2f}")
        
        if generations_without_improvement > stagnation_limit // 2:
             mutation_rate = min(0.4, mutation_rate * 1.05) # Slower increase, lower cap
        else:
             mutation_rate = max(0.05, mutation_rate * 0.98) # Slower decrease
        print(f"Generation {generation}: Mutation rate: {mutation_rate:.2f}, Temperature: {temperature:.2f}")

        # --- Restart Mechanism --- 
        if generations_without_improvement >= stagnation_limit:
            print(f"Stagnation detected! Restarting {population_size // 3} individuals.")
            num_to_keep = population_size * 2 // 3 
            population = sorted(population, key=fitness)
            elite_kept = population[:top_n_elitism] 
            rest_kept = population[top_n_elitism:num_to_keep]
            new_random = initialization(population_size - num_to_keep)
            population = elite_kept + rest_kept + new_random
            generations_without_improvement = 0 
            temperature = initial_temperature * 0.8 
            penalties = [fitness(schedule) for schedule in population] 
            print("Restart complete.")

        sorted_population = [x for _, x in sorted(zip(penalties, population), key=lambda pair: pair[0])]
        elite_individuals = elitism(sorted_population, top_n=top_n_elitism)

        selected_parents = tournament_selection(population, tournament_size=tournament_size)

        offspring = []
        parent_idx = 0
        while len(offspring) < population_size - len(elite_individuals) and parent_idx + 1 < len(selected_parents):
            parent1, parent2 = selected_parents[parent_idx], selected_parents[parent_idx + 1]
            parent_idx += 2
            
            children = []
            if random.random() < crossover_probability:
                child1 = crossover_method(parent1, parent2)
                child2 = crossover_method(parent2, parent1)
                children.extend([child1, child2])
            else:
                children.extend([parent1.copy(), parent2.copy()])
                
            for child in children:
                if random.random() < mutation_rate:
                    mutated_child = mutation_method(child)
                else:
                    mutated_child = child
                
                original_penalty = fitness(child) 
                mutated_penalty = fitness(mutated_child)
                delta_penalty = mutated_penalty - original_penalty
                
                if delta_penalty < 0: 
                    offspring.append(mutated_child)
                else:
                    if temperature > 1.0: 
                        acceptance_probability = math.exp(-delta_penalty / temperature)
                        if random.random() < acceptance_probability:
                            offspring.append(mutated_child) 
                        else:
                            offspring.append(child) 
                    else:
                        offspring.append(child) 

        population = elite_individuals + offspring
        population = population[:population_size] 
        
        if generation % local_search_frequency == 0 and generation > 0:
            print(f"Applying refined local search to top {top_n_elitism} individuals...")
            population = sorted(population, key=fitness)
            for i in range(top_n_elitism):
                population[i] = local_search_refined(population[i]) 
            print("Local search complete.")

        temperature *= cooling_rate
        temperature = max(temperature, 0.1)

    final_sorted_population = sorted(population, key=fitness)
    
    if best_solution_ever is not None and best_penalty_ever < fitness(final_sorted_population[0]):
        if not any(fitness(ind) == best_penalty_ever for ind in final_sorted_population):
            final_sorted_population.insert(0, best_solution_ever)
            final_sorted_population = final_sorted_population[:population_size]

    return final_sorted_population, penalties_per_generation

