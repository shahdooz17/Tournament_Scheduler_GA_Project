import streamlit as st
from scheduler.genetic_algo import genetic_algorithm
from scheduler.initialization import initialization
from scheduler.compare import compare_random_vs_optimized
from scheduler.crossover import order_crossover, cyclic_crossover
from scheduler.mutation import swap_mutation, scramble_mutation

def main():
    st.title("🏆 Sports Tournament Scheduling with Genetic Algorithm")

    st.header("⚙️ Configuration")

    population_size = st.slider("Population Size", min_value=5, max_value=100, value=30, step=5)
    generations = st.slider("Number of Generations", min_value=10, max_value=1000, value=200, step=10)

    crossover_choice = st.selectbox(
        "Select Crossover Method",
        options=["Order Crossover", "Cyclic Crossover"],
        index=0
    )

    mutation_choice = st.selectbox(
        "Select Mutation Method",
        options=["Swap Mutation", "Scramble Mutation"],
        index=0
    )
    
    # Add sliders for GA parameters
    mutation_rate = st.slider("Initial Mutation Rate", min_value=0.1, max_value=0.5, value=0.2, step=0.05)
    crossover_rate = st.slider("Crossover Rate", min_value=0.7, max_value=1.0, value=0.9, step=0.05)
    tournament_size = st.slider("Tournament Size", min_value=2, max_value=5, value=2, step=1)
    elitism_count = st.slider("Elitism Count", min_value=1, max_value=5, value=1, step=1)

    crossover_method = order_crossover if crossover_choice == "Order Crossover" else cyclic_crossover
    mutation_method = swap_mutation if mutation_choice == "Swap Mutation" else scramble_mutation

    if st.button("Generate Optimized Schedule"):
        # Create a diverse initial population
        initial_population = initialization(population_size)

        optimized_population, penalties_per_gen = genetic_algorithm(
            population_size=population_size,
            generations=generations,
            crossover_method=crossover_method,
            mutation_method=mutation_method,
            initial_mutation_rate=mutation_rate,
            crossover_probability=crossover_rate,
            tournament_size=tournament_size,
            top_n_elitism=elitism_count,
            initial_population=initial_population
        )

        optimized_schedule = optimized_population[0]
        
        # Generate a random schedule for comparison
        random_schedule = initialization(1)[0]

        comparison = compare_random_vs_optimized(random_schedule, optimized_schedule)

        st.header("🔍 Results")

        st.write(f"🔹 Random Schedule Penalty: **{comparison['Random Schedule Penalty']}**")
        st.write(f"✅ Optimized Schedule Penalty: **{comparison['Optimized Schedule Penalty']}**")
        st.write(f"📉 Improvement: **{comparison['Improvement in Penalty']}**")

        st.subheader("🗓️ Random Schedule")
        st.dataframe(comparison["Random Schedule Data"])

        st.subheader("🏆 Optimized Schedule")
        st.dataframe(comparison["Optimized Schedule Data"])

        st.subheader("📈 Penalty Progress Over Generations")
        st.line_chart(penalties_per_gen)

if __name__ == "__main__":
    main()
