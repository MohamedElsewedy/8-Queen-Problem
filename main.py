import random

N = 8
POPULATION_SIZE = 100  
MUTATION_RATE = 0.2  
GENERATIONS = 1000  


def fitness(board):
    non_attacking_pairs = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] != board[j] and abs(board[i] - board[j]) != abs(i - j):
                non_attacking_pairs += 1
    return non_attacking_pairs


def create_individual():
    return [random.randint(0, N - 1) for _ in range(N)]


def create_population():
    return [create_individual() for _ in range(POPULATION_SIZE)]


def select(population):
    weights = [fitness(individual) for individual in population]
    total_fitness = sum(weights)
    probabilities = [w / total_fitness for w in weights]
    return random.choices(population, probabilities, k=2)


def crossover(parent1, parent2):
    point = random.randint(0, N - 1)
    child = parent1[:point] + parent2[point:]
    return child


def mutate(individual):
    if random.random() < MUTATION_RATE:
        individual[random.randint(0, N - 1)] = random.randint(0, N - 1)
    return individual


def is_solution(individual):
    return fitness(individual) == (N * (N - 1)) // 2


def print_board(board):
    for row in range(N):
        line = ""
        for col in range(N):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()


def genetic_algorithm():
    population = create_population()
    for generation in range(GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1, parent2 = select(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

        for individual in population:
            if is_solution(individual):
                print(f"Solution found in generation {generation + 1}: {individual}")
                print_board(individual)
                return

        if generation % 100 == 0:
            best_fitness = max(fitness(ind) for ind in population)
            print(f"Generation {generation + 1}, Best Fitness: {best_fitness}")

    print("No solution found after maximum generations.")


genetic_algorithm()
