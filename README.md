# 🏆 Sports Tournament Scheduler using Genetic Algorithms

This project aims to build an intelligent scheduling tool for sports tournaments using **Genetic Algorithms (GA)** and other **Evolutionary Algorithms (EA)** or **Swarm Intelligence (SI)** techniques. The system will optimize tournament schedules by minimizing constraint violations such as venue clashes, unfair rest periods, and unbalanced match distributions.

---

## 📌 Project Goals

- Represent tournament formats (e.g., round-robin, knockout) as individuals in a population.

- Apply evolutionary methods to generate feasible and optimized schedules.

- Implement constraint handling using repair, penalty, or decoder functions.

- Visualize schedules using charts and tables.

- Compare multiple GA configurations to evaluate performance.

---

## 🧰 Libraries & Tools

| Purpose                        | Library/Tool     |
|-------------------------------|------------------|
| Genetic Algorithms / EAs      | `DEAP`, `PyGAD`  |
| Constraint Modeling           | `NumPy`, `PuLP`  |
| Visualization                 | `Matplotlib`, `Plotly`, `Pandas` |
| GUI                           | `Tkinter`, `Streamlit` |
| Data Handling & Utils         | `Pandas`, `JSON` |
| Logging & Experimentation     | `logging`, `SciPy`, `PrettyTable` |
| Optional SI Methods           | `pyswarms`       |
---

## 📁 Folder Structure
```
tournament-scheduler-ga/
│
├── 📁 src/                       
│   ├── __init__.py
│   ├── main.py                  
│   ├── scheduler/                 
│   │   ├── __init__.py
│   │   ├── representation.py     
│   │   ├── fitness.py             
│   │   ├── selection.py           
│   │   ├── crossover.py           
│   │   ├── mutation.py            
│   │   ├── survivor.py            
│   │   ├── initialization.py      
│   │   ├── termination.py        
│   │   └── constraints.py         
│   ├── experiments/              
│   │   ├── experiment_runner.py
│   │   ├── coevolution.py
│   │   └── config.py              
│   └── utils/                    
│       ├── visualizer.py         
│       ├── helpers.py
│       └── logger.py
│
├── 📁 data/                       
│   └── teams.json
│
├── 📁 results/                    
│   ├── logs/
│   ├── plots/
│   └── schedules/
│
├── 📁 gui/                        
│   └── streamlit_app.py
│
├── 📁 docs/                      
│   └── report.md
│
├── .gitignore
├── README.md                     
├── requirements.txt              
└── setup.py                     

```
## 💡 Suggested Approach

1. **Problem Formalization**  
   - Define this as a **constrained optimization** problem.

2. **GA Components**  
   - Representation: schedule as an ordered list of matches  
   - Fitness: based on venue conflicts, rest periods, match fairness  
   - Selection: Tournament selection, Roulette wheel  
   - Crossover: Order crossover (OX), Partially Matched (PMX)  
   - Mutation: Swap mutation, Insertion mutation  
   - Survivor Selection: Generational vs. steady-state  
   - Constraint Handling: Penalty functions or repair functions  

3. **Comparison Strategy**  
   - Test multiple configurations of GA (mutation, crossover, selection, population size)  
   - Visualize results using convergence graphs  
   - Compare generated schedules to a greedy baseline  

---

## 🗓️ Project Timeline

| Date           | Milestone                                   |
|----------------|---------------------------------------------|
| **Apr 20 - 22** | Project setup, requirements, repo creation |
| **Apr 23 - 25** | GA components: representation, fitness     |
| **Apr 26 - 28** | Constraint handling + variation operators   |
| **Apr 29 - May 1** | Selection, survivor models, initialization |
| **May 2 - 4**   | Run experiments, visualize results         |
| **May 5 - 7**   | GUI/dashboard (optional), polish code      |
| **May 8 - 10**  | Final report, testing, and documentation   |

---

## 📋 Deliverables

- ✅ Python-based prototype for tournament scheduling  
- ✅ Constraint-aware evolutionary optimization  
- ✅ Multiple GA configurations with result comparisons  
- ✅ Visual charts and reports  
- ✅ Final write-up with findings and future work

---

## 👨‍💻 Author

Built with ❤️ using Python, Evolutionary Algorithms, and Data Visualization.



