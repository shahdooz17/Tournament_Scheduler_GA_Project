def cyclic_crossover(parent1, parent2):
    size = len(parent1)
    child1 = [None] * size
    child2 = [None] * size

    visited = [False] * size

    cycle = 0
    while any(not visited[i] for i in range(size)): 
        current_idx = 0

        while visited[current_idx]:
            current_idx += 1

        cycle_start = current_idx
        while not visited[cycle_start]:
            if cycle % 2 == 0:
                child1[cycle_start] = parent1[cycle_start]
                child2[cycle_start] = parent2[cycle_start]
            else:
                child1[cycle_start] = parent2[cycle_start]
                child2[cycle_start] = parent1[cycle_start]

            visited[cycle_start] = True
            cycle_start = parent2.index(parent1[cycle_start])  

        cycle += 1

    return child1, child2



# Example parents
parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
parent2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]

# Perform cycle crossover
child1, child2 = cyclic_crossover(parent1, parent2)

print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child 1:", child1)
print("Child 2:", child2)
