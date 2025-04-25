from scheduler.fitness import fitness

def elitism(population, top_n=5): 
    
    population.sort(key=lambda ind: fitness(ind))
    best_individuals = population[:top_n]
    
    return best_individuals