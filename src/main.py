import streamlit as st
import random
import pandas as pd

from scheduler.initialization import initialization
from scheduler.fitness import fitness
from scheduler.crossover import order_crossover
from scheduler.mutation import swap_mutation
from scheduler.selection import tournament_selection
from scheduler.survivor import elitism
from scheduler.compare import compare_random_vs_optimized

# Constants
POPULATION_SIZE = 10
MAX_GENERATIONS = 200
MUTATION_PROBABILITY = 0.1
TOURNAMENT_SIZE = 2
TOP_N_ELITISM = 1

def genetic_algorithm(population_size=POPULATION_SIZE, generations=MAX_GENERATIONS):
    population = initialization(population_size)

    for generation in range(generations):
        if generation % 10 == 0:
            st.text(f"Generation {generation + 1}")

        penalties = [fitness(schedule) for schedule in population]
        sorted_population = [x for _, x in sorted(zip(penalties, population), key=lambda pair: pair[0])]

        elite_individuals = elitism(sorted_population, top_n=TOP_N_ELITISM)
        selected_parents = tournament_selection(population, tournament_size=TOURNAMENT_SIZE)

        offspring = []
        for i in range(0, len(selected_parents), 2):
            if i + 1 < len(selected_parents):
                parent1, parent2 = selected_parents[i], selected_parents[i + 1]
                child1 = order_crossover(parent1, parent2)
                child2 = order_crossover(parent2, parent1)
                offspring.extend([child1, child2])
            else:
                offspring.append(selected_parents[i])

        mutated_offspring = []
        for child in offspring:
            if random.random() < MUTATION_PROBABILITY:
                mutated_offspring.append(swap_mutation(child))
            else:
                mutated_offspring.append(child)

        population = elite_individuals + mutated_offspring
        population = population[:population_size]

    sorted_population = sorted(population, key=fitness)

    # Ensure correct number of individuals returned
    while len(sorted_population) < population_size:
        sorted_population.append(random.choice(sorted_population))

    return sorted_population[:population_size]

def display_schedule(schedule, idx, title="Schedule"):
    penalty = fitness(schedule)
    schedule_data = [{
        "Team 1": match['team1'],
        "Team 2": match['team2'],
        "Day": match['day'],
        "Time": match['time'],
        "Venue": match['venue']
    } for match in schedule]

    schedule_df = pd.DataFrame(schedule_data)
    st.subheader(f"{title} {idx + 1}")
    st.dataframe(schedule_df)
    st.write(f"Penalty: {penalty}")

def main():
    st.title("Sports Tournament Scheduling")

    num_individuals = st.slider("Select Number of Schedules", min_value=1, max_value=20, value=5)

    if st.button("Generate Schedules"):
        random_schedules = initialization(num_individuals)
        optimized_schedules = genetic_algorithm(population_size=num_individuals)

        num_to_compare = min(len(random_schedules), len(optimized_schedules))

        for idx in range(num_to_compare):
            comparison = compare_random_vs_optimized(random_schedules[idx], optimized_schedules[idx])

            st.markdown(f"### 🔄 Comparison {idx + 1}")
            st.write(f"🔹 Random Schedule Penalty: **{comparison['Random Schedule Penalty']}**")
            st.write(f"✅ Optimized Schedule Penalty: **{comparison['Optimized Schedule Penalty']}**")
            st.write(f"📉 Improvement: **{comparison['Improvement in Penalty']}**")

            st.subheader("🗓️ Random Schedule")
            st.dataframe(comparison["Random Schedule Data"])

            st.subheader("🏆 Optimized Schedule")
            st.dataframe(comparison["Optimized Schedule Data"])

    
if __name__ == "__main__":
    main()