import streamlit as st
from scheduler.genetic_algo import genetic_algorithm
from scheduler.initialization import initialization
from scheduler.compare import compare_random_vs_optimized

def main():
    st.title("🏆 Sports Tournament Scheduling with Genetic Algorithm")

    num_individuals = st.slider("Select Number of Schedules", min_value=1, max_value=20, value=5)

    if st.button("Generate Schedules"):
        random_schedules = initialization(num_individuals)

        optimized_schedules, penalties_per_gen = genetic_algorithm(population_size=num_individuals)

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

        st.subheader("📉 Penalty Progress Over Generations")
        st.line_chart(penalties_per_gen)

if __name__ == "__main__":
    main()
