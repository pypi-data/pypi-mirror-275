import numpy as np

def one_point_crossover(chromosome1 , chromosome2):

    assert len(chromosome1)==len(chromosome2)
    length = len(chromosome1)
    cross_point = np.random.randint(1,length-1)

    child1 = chromosome1[:cross_point]+chromosome2[cross_point:]
    child2 = chromosome2[:cross_point]+chromosome1[cross_point:]

    return child1 , child2


def multiple_point_crossover(chromosome1,chromosome2,number_of_cross_points=2):

    assert len(chromosome1)==len(chromosome2)
    length = len(chromosome1)
    cross_points = [0]

    for _ in range(number_of_cross_points):

        cross_point = np.random.randint(1,length-1)

        while(cross_point in cross_points):
            cross_point = np.random.randint(1,length-1)
        
        cross_points.append(cross_point)

    cross_points.append(length)
    cross_points.sort()


    child1 = []
    child2 = []
    n = len(cross_points)
    i = 0

    while (i < n - 1):

        if(i==n-2):
            
            child1 += chromosome1[cross_points[i]:cross_points[i+1]]
            child2 += chromosome2[cross_points[i]:cross_points[i+1]]

            break

        child1 += chromosome1[cross_points[i]:cross_points[i+1]]
        child1 += chromosome2[cross_points[i+1]:cross_points[i+2]]

        child2 += chromosome2[cross_points[i]:cross_points[i+1]]
        child2 += chromosome1[cross_points[i+1]:cross_points[i+2]]

        i += 2


    return child1,child2

def uniform_crossover(chromosome1,chromosome2):

    assert len(chromosome1)==len(chromosome2)
    length = len(chromosome1)

    choices = [True , False]

    child1 = []
    child2 = []

    for i in range(length):

        choice = np.random.choice(choices)

        if choice : 

            child1.append(chromosome1[i])
            child2.append(chromosome2[i])

        else: 

            child1.append(chromosome2[i])
            child2.append(chromosome1[i])

    return child1,child2


def arithmetic_recombination(chromosome1,chromosome2,a=0.5):

    assert ((len(chromosome1) == len(chromosome2))and((a>=0 and a<=1))and((type(chromosome1)!=str)or(type(chromosome1)!=str)))

    chromosome1 = np.array(chromosome1)
    chromosome2 = np.array(chromosome2)

    child1 = np.add(np.dot(a,chromosome1),np.dot((1-a),chromosome2))
    child2 = np.add(np.dot(a,chromosome2),np.dot((1-a),chromosome1))

    return child1 , child2


def partially_mapped_crossover(chromosome1,chromosome2):

    assert (len(chromosome1)==len(chromosome2))
    length = len(chromosome1)
    
    cross_points = []

    for _ in range(2):

        cross_point = np.random.randint(1,length-1)

        while(cross_point in cross_points):
            cross_point = np.random.randint(1,length-1)
        
        cross_points.append(cross_point)

    cross_points.sort()

    if(type(chromosome1)==int):

        child1 = np.zeros(length)
        child2 = np.zeros(length)

    elif(type(chromosome1)==str):
        
        child1 = ['#' for i in range(length)]
        child2 = ['#' for i in range(length)]

    mid1 = chromosome2[cross_points[0]:cross_points[1]]
    mid2 = chromosome1[cross_points[0]:cross_points[1]]
    mid_length = len (mid1)


    child1[cross_points[0]:cross_points[1]] = mid1
    child2[cross_points[0]:cross_points[1]] = mid2


    for i in range(length):

        if(i>=cross_points[0] and i<cross_points[1]): continue

        for j in range(mid_length):

            if(chromosome1[i] == mid1[j]):

                child1[i] = mid2[j]

                break

            elif(j==(mid_length-1)):

                child1[i] = chromosome1[i]

        for j in range(mid_length):

            if(chromosome2[i] == mid2[j]):

                child2[i] = mid1[j]

                break

            elif(j==(mid_length-1)):

                child2[i] = chromosome2[i]



    return child1 , child2


def ordered_crossover(chromosome1,chromosome2):

    assert (len(chromosome1)==len(chromosome2))
    length = len(chromosome1)
    
    cross_points = []
    genes1 = []
    genes2 = []

    if(type(chromosome1)==int):

        child1 = np.zeros(length)
        child2 = np.zeros(length)

    elif(type(chromosome1)==str):
        
        child1 = ['#' for i in range(length)]
        child2 = ['#' for i in range(length)]


    for _ in range(2):

        cross_point = np.random.randint(1,length-1)

        while(cross_point in cross_points):
            cross_point = np.random.randint(1,length-1)
        
        cross_points.append(cross_point)

    cross_points.sort()

    mid1 = chromosome2[cross_points[0]:cross_points[1]]
    mid2 = chromosome1[cross_points[0]:cross_points[1]]
    mid_length = len (mid1)


    child1[cross_points[0]:cross_points[1]] = mid1
    child2[cross_points[0]:cross_points[1]] = mid2

    for i in range(cross_points[1],length):

        genes1.append(chromosome1[i])
        genes2.append(chromosome2[i])

    for i in range(cross_points[0]):

        genes1.append(chromosome1[i])
        genes2.append(chromosome2[i])

    for i in range(cross_points[0],cross_points[1]):

        genes1.append(chromosome1[i])
        genes2.append(chromosome2[i])

    final_genes1 = []
    final_genes2 = []

    for i in range(len(genes1)):

        for j in range(mid_length):

            if(genes1[i]==mid1[j]):

                break

            elif(j == mid_length -1):final_genes1.append(genes1[i])        
            
    
    for i in range (len(genes2)):

        for j in range(mid_length):

            if(genes2[i]==mid2[j]):

                break
            
            elif(j == mid_length -1):final_genes2.append(genes2[i])


    for i in range(cross_points[1],length):

        child1[i] = final_genes1[i-cross_points[1]]
        child2[i] = final_genes2[i-cross_points[1]]

    for i in range(cross_points[0]):

        child1[i] = final_genes1[i+(length-cross_points[1])]
        child2[i] = final_genes2[i+(length-cross_points[1])]


    return child1 , child2


def cyclic_crossover(chromosome1,chromosome2):

    assert (len(chromosome1)==len(chromosome2))
    length = len(chromosome1)

    if(type(chromosome1)==int):

        child1 = np.full(length,np.inf)
        child2 = np.full(length,np.inf)

    elif(type(chromosome1)==str):
        
        child1 = ['#' for i in range(length)]
        child2 = ['#' for i in range(length)]

    first_element = chromosome1[0]
    element = chromosome2[0]

    child1[0] = first_element
    child2[0] = element

    while(first_element != element):

        index = chromosome1.index(element)
        element1 = chromosome1[index]
        element = chromosome2[index]

        child1[index] = element1
        child2[index] = element

    if(type(chromosome1)==int):

        for i in range(length):

            if(child1[i] != np.inf):

                continue

            else:

                child1[i] = chromosome2[i]
                child2[i] = chromosome1[i]
    
    if(type(chromosome1)==str):

        for i in range(length):

            if(child1[i] != '#'):

                continue

            else:

                child1[i] = chromosome2[i]
                child2[i] = chromosome1[i]

    return child1 , child2



def shuffle_crossover(chromosome1,chromosome2):

    assert len(chromosome1)==len(chromosome2)
    length = len(chromosome1)
    cross_point = np.random.randint(1,length-1)

    part1_1 = chromosome1[:cross_point]
    part1_2 = chromosome1[cross_point:]
    part2_1 = chromosome2[:cross_point]
    part2_2 = chromosome2[cross_point:]

    np.random.shuffle(part1_1)
    np.random.shuffle(part1_2)
    np.random.shuffle(part2_1)
    np.random.shuffle(part2_2)

    child1 = part2_1 + part1_2
    child2 = part1_1 + part2_2

    return child1 ,child2