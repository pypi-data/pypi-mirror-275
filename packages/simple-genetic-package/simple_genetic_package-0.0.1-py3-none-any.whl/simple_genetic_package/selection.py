from random import random

def stochastic_universal_sampling(population, fitness_func, children_to_keep_num):
    sum = 0
    smallest_fitness = 0
    fitnesses = []

    #handling negative fitnesses
    for individual in population:
        fitness = fitness_func(individual)
        if(fitness<smallest_fitness):
            smallest_fitness = fitness
        fitnesses.append(fitness)

    for fitness in fitnesses:
        sum += (fitness + (-smallest_fitness))

        

    p = sum / children_to_keep_num
    start = random() * p

    points = []
    index = 0

    for i in range(children_to_keep_num):
        points.append(start + (p*i))

    children_to_keep = []
    sum = 0

    for individual in population:
        sum += (fitness_func(individual) + (-smallest_fitness))

        while(index<len(points) and sum>=points[index]):
            children_to_keep.append(individual)
            index+=1

    return children_to_keep


def elitist_selection(population, fitness_func, children_to_keep_num):
    population_with_fitness = [(individual, fitness_func(individual)) for individual in population]
    population_with_fitness = sorted(population_with_fitness, key=lambda x: x[1])
    children_to_keep = []
    for i in range(children_to_keep_num):
        children_to_keep.append(population_with_fitness.pop()[0])
    return children_to_keep
        
