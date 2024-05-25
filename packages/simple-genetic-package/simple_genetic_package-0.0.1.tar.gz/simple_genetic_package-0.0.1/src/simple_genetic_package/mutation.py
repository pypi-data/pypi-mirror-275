import numpy as np
from copy import deepcopy


def sorted_random_numbers(point_nums, interval):
    """
    Returns several sorted random integers in an interval.
    point_nums: number of points to be selected.
    interval: the interval which the numbers are selected.
    """    
    points = []
    for _ in range(point_nums):
        num = np.random.randint(0, abs(interval))
        while num in points:
            num = np.random.randint(0, abs(interval))
        points.append(num)
    return sorted(points)


def integer_chrom_generator(n):
    """
    Produces chromosomes with integer values for each gene. (integer alleles)
    n: The length of the chromosome to be produced 
    """  
    a = []
    for _ in range(n):
        rand = np.random.randint(0, n)
        while rand in a:
            rand = np.random.randint(0, n)
        else:
            a.append(rand)
    return np.array(a)


def binary_chrom_generator(n, zero_prob, one_prob): 
    """
    Produces chromosomes with binary values for each gene. (binary alleles)
    n: The length of the chromosome to be produced 
    zero_prob: The probability for the allele to be zero
    one_prob: The probability for the allele to be one
    """   
    return np.random.choice([0, 1], size=n, p=[zero_prob, one_prob])


def bit_flip_mutation(parent, pm):
    """
    This function takes one chromosome, and performs Bit flip mutation on it. 
    parent_one: The parent
    pm: The probability of mutation
    """ 

    chrom_length = len(parent)
    child_one = np.array([-1]*chrom_length)  

    if np.random.rand() < pm:  # if pm is greater than random number
        point_nums = np.random.randint(1, 4)
        points = sorted_random_numbers(point_nums, chrom_length)

        for i in range(point_nums): #performing XOR, to flip the bits in the chosen points
            parent[points[i]] = parent[points[i]] ^ 1
        child_one = parent

    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent)

    return child_one


def random_resetting_mutation(parent_one, pm):
    """
    This function takes one chromosome, and performs Random resetting mutation on it. 
    parent_one: The parent
    pm: The probability of mutation
    """ 
    parent_one = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) 

    chrom_length = len(parent_one)
    child_one =  np.array([-1]*chrom_length)

    if np.random.rand() < pm:  # if pm is greater than random number
        point_nums = np.random.randint(1, 4)
        points = sorted_random_numbers(point_nums, chrom_length)

        for i in range(len(points)): 
            parent_one[points[i]] = np.random.randint(1, 10) #one of the admissible values
        child_one = parent_one

    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)
    
    return child_one


def swap_mutation(parent_one, pm):
    """
    This function takes one chromosome, and performs Swap mutation on it. 
    parent_one: The parent
    pm: The probability of mutation
    """ 


    chrom_length = len(parent_one)
    child_one =  np.array([-1]*chrom_length) 

    if np.random.rand() < pm:  # if pm is greater than random number
        points = sorted_random_numbers(2, chrom_length)    
        parent_one[points[0]], parent_one[points[1]] = parent_one[points[1]], parent_one[points[0]] 
        child_one = parent_one

    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)
    
    return child_one


def scramble_mutation(parent_one, pm):
    """
    This function takes one chromosome, and performs Scramble mutation on it. 
    parent_one: The parent
    pm: The probability of mutation
    """ 

    chrom_length = len(parent_one)
    child_one = np.array([-1]*chrom_length)  

    if np.random.rand() < pm:  # if pm is greater than random number
        points = sorted_random_numbers(2, chrom_length)   
        permute = []
        child_one = parent_one
        for i in range(points[0], points[1]):
            permute.append(parent_one[i])
        np.random.shuffle(permute)
        k = 0
        for i in range(points[0], points[1]):
            child_one[i] = permute[k]
            k+=1      
        
    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)

    
    return child_one


def inversion_mutation(parent_one, pm):
    """
    This function takes one chromosome, and performs Inversion mutation on it. 
    parent_one: The parent
    pm: The probability of mutation
    """ 

    chrom_length = len(parent_one)
    child_one =  np.array([-1]*chrom_length) 

    if np.random.rand() < pm:  # if pm is greater than random number
        points = sorted_random_numbers(2, chrom_length)  
        reverse_list = []
        child_one = parent_one
        for i in range(points[0], points[1]):
            reverse_list.append(parent_one)
        reverse_list.reverse()
        k = 0
        for i in range(points[0], points[1]):
            child_one[i] = reverse_list[k]
            k+=1      
         
    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)
    
    return child_one


def inorder_mutation(parent_one, pm):
    """
    This function takes one chromosome, and performs Inorder mutation on it. 
    parent_one: The parent
    pm: The probability of mutation
    """ 
    

    chrom_length = len(parent_one)
    child_one = genes= np.array([-1]*chrom_length) 

    if np.random.rand() < pm:  # if pm is greater than random number
        point_nums = np.random.randint(1, 5) #selecting one to four elements 
        points = sorted_random_numbers(point_nums, chrom_length)
        child_one = parent_one
  
        for i in range(point_nums):
            w = np.random.uniform(low=0, high=1)
            if w < 0.5:
                child_one[points[i]] = child_one[points[i]] ^ 1 #flipping the bit

    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)
    
    return child_one

def center_inversion_mutation(parent_one, pm):
    """
    This function takes one chromosome, and performs Center inversion mutation on it. 
    Length of the chromosome in this mutation should be more than 4.
    parent_one: The parent
    pm: The probability of mutation
    """ 

   
    chrom_length = len(parent_one)
    child_one = np.array([-1]*chrom_length) 

    if np.random.rand() < pm:  # if pm is greater than random number
        reverse_list1 = []
        reverse_list2 = []
        point = np.random.randint(2,chrom_length-1) #break point  
        child_one = parent_one
        for i in range(chrom_length):
            if i < point:
                reverse_list1.append(parent_one[i])
            else:
                reverse_list2.append(parent_one[i])
        reverse_list1.reverse()
        reverse_list2.reverse()

        for i in range(point): #Filling the first half
            child_one[i] = reverse_list1[i]
        k = 0
        for i in range(point, chrom_length): #Filling the first half
            child_one[i] = reverse_list2[k]
            k+=1
                
    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)
    

    return child_one


def throas_mutation(parent_one, pm):
    """
    This function takes one chromosome, and performs Throas mutation on it. 
    Last ==> First
    Second ==> Last
    First ==> Second 
    parent_one: The parent
    pm: The probability of mutation
    """ 


    chrom_length = len(parent_one)
    child_one = np.array([-1]*chrom_length)   

    if np.random.rand() < pm:  # if pm is greater than random number
        interval = []
        point1 = np.random.randint(0,chrom_length-3)
        point2 = point1 + 3
        child_one = parent_one
        for i in range(point1, point2):
            interval.append(child_one[i])
        interval_copy = interval.copy()
        interval[0] = interval_copy[-1] 
        interval[-1] = interval_copy[1] 
        interval[1] = interval_copy[0] 
        k = 0
        for i in range(point1, point2):
            child_one[i] = interval[k]
            k+=1

    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)
    
    return child_one

def thrors_mutation(parent_one, pm):
    """
    This function takes one chromosome, and performs Thrors mutation on it. 
    Last ==> First
    Second ==> Last
    First ==> Second 
    In compare to Throas mutation, in Thrors mutation, the chosen elements are not necessarily 
    successive. 
    parent_one: The parent
    pm: The probability of mutation
    """ 

   
    chrom_length = len(parent_one)
    child_one = np.array([-1]*chrom_length)

    if np.random.rand() < pm:  # if pm is greater than random number
        elements = []
        points = sorted_random_numbers(3, chrom_length)
        child_one = parent_one

        for i in range(len(points)): #selecting the elements
            elements.append(parent_one[points[i]]) 
        elements_copy = elements.copy()
        elements[0] = elements_copy[-1] 
        elements[-1] = elements_copy[1] 
        elements[1] = elements_copy[0] 
        k = 0
        for i in range(chrom_length):
            if i in points:
                child_one[i] = elements[k]
                k+=1
    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)
    
    return child_one


def distance_based_mutation(parent_one, pm):
    """
    This function takes one chromosome, and performs Distance based mutation on it.
    In this method, g is the position for the chosen gene. d is the distance from that position. 
    parent_one: The parent
    pm: The probability of mutation
    """ 

    chrom_length = len(parent_one)
    child_one = np.array([-1]*chrom_length)

    if np.random.rand() < pm:  # if pm is greater than random number
        interval = []
        d = np.random.randint(1, 4)
        g = np.random.randint(d,chrom_length-d)
        child_one = parent_one
        for i in range(g - d, g + d + 1): #element in position g and d elements in each direction
            interval.append(parent_one[i]) 
        np.random.shuffle(interval)
        k = 0
        for i in range(g - d, g + d + 1): #Replacing elements
            child_one[i] = interval[k]
            k+=1


    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)
    
    return child_one


def displacement_mutation(parent_one, pm):
    """
    This function takes one chromosome, and performs Displacement mutation on it. 
    parent_one: The parent
    pm: The probability of mutation
    """ 

    chrom_length = len(parent_one)
    child_one =  np.array([-1]*chrom_length)

    if np.random.rand() < pm:  # if pm is greater than random number
        interval = []
        points = sorted_random_numbers(2, chrom_length)
        duplicate = parent_one.tolist().copy() 
        for i in range(points[0], points[1]):
            interval.append(parent_one[i])
        for i in range(chrom_length):
            if parent_one[i] in interval:
                duplicate.remove(parent_one[i])
   
        # (duplicate)
        lists = []
        for i in range(len(duplicate) + 1):
            a = []
            lists.append(a)
        position = np.random.randint(0, len(duplicate) + 1) #the position of the paste
        for i in range(len(interval)):
            lists[position].append(interval[i])
        k = 0
        for i in range(len(lists)):
            if not lists[i]: #if lists[i] is empty
                lists[i].append(duplicate[k])
                k+=1
        flat_list = [item for sublist in lists for item in sublist]
        child_one = np.array(flat_list)

    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)

    return child_one


def insertion_mutation(parent_one, pm):
    """
    This function takes one chromosome, and performs Insertion mutation on it. 
    parent_one: The parent
    pm: The probability of mutation
    """ 

    chrom_length = len(parent_one)
    child_one = np.array([-1]*chrom_length)   

    if np.random.rand() < pm:  # if pm is greater than random number
        point = np.random.randint(0, chrom_length) #picking one gene
   
        duplicate = parent_one.tolist().copy()         
        duplicate.remove(parent_one[point]) 

        
        lists = []
        for i in range(len(duplicate) + 1):
            a = []
            lists.append(a)
        position = np.random.randint(0, len(duplicate) + 1) #the position of the paste
        lists[position].append(parent_one[point])
        k = 0
        for i in range(len(lists)):
            if not lists[i]: #if lists[i] is empty
                lists[i].append(duplicate[k])
                k+=1
        flat_list = [item for sublist in lists for item in sublist]
        child_one = np.array(flat_list)

    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)

    
    return child_one


def displaced_inversion_mutation(parent_one, pm):
    """
    This function takes one chromosome, and performs Displaced inversion mutation on it. 
    parent_one: The parent
    pm: The probability of mutation
    """ 

    chrom_length = len(parent_one)
    child_one = np.array([-1]*chrom_length)   

    if np.random.rand() < pm:  # if pm is greater than random number
        interval = []
        points = sorted_random_numbers(2, chrom_length)
        duplicate = parent_one.tolist().copy() 
        for i in range(points[0], points[1]):
            interval.append(parent_one[i])
        for i in range(chrom_length):
            if parent_one[i] in interval:
                duplicate.remove(parent_one[i])
   
        # (duplicate)
        lists = []
        for i in range(len(duplicate) + 1):
            a = []
            lists.append(a)
        position = np.random.randint(0, len(duplicate) + 1) #the position of the paste
        interval.reverse()
        for i in range(len(interval)):
            lists[position].append(interval[i])

        k = 0
        for i in range(len(lists)):
            if not lists[i]: #if lists[i] is empty
                lists[i].append(duplicate[k])
                k+=1
        flat_list = [item for sublist in lists for item in sublist]
        child_one = np.array(flat_list)

    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)

    return child_one


def creep_mutation(parent_one, pm):
    """
    This function takes one chromosome, and performs Creep mutation on it. 
    parent_one: The parent
    pm: The probability of mutation
    """ 

    chrom_length = len(parent_one)
    child_one =  np.array([0.0]*chrom_length)

    if np.random.rand() < pm:  # if pm is greater than random number
        point = np.random.randint(0, chrom_length)   
        child_one = parent_one 
        child_one[point] = round(np.random.uniform(low=0.1, high=0.95), 3)

    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)
    
    return child_one


def calculate_mask(chrom_size, px):
    """
    This method, performs the mask calculation for the Uniform crossover.
    chrom_size: The mask has the same size of the chromosome.
    px: A control parameter for the number of ones in the mask vector.
    """  
    mask = [0]*chrom_size
    for i in range(chrom_size):
        prob = np.random.rand()
        if prob <= px:
            mask[i]=1
    return mask


def uniform_random_mutation(parent_one, pm, chrom_type):
    """
    parent_one: The parent
    pm: The probability of mutation
    """ 


    chrom_length = len(parent_one)

    
    if chrom_type == "float":
        random_genes = np.round(np.random.uniform(0.0, 1.0, chrom_length), 3)
        parent_two =  random_genes
        child_one = np.array([0.0]*chrom_length)  
    
    elif chrom_type == "integer":
        random_genes = integer_chrom_generator(chrom_length)
        parent_two =  random_genes
        child_one =  np.array([-1]*chrom_length)   
    
    else: # binary individual
        random_genes = np.array(binary_chrom_generator(chrom_length, 0.5, 0.5))
        parent_two =  random_genes
        child_one =  np.array([-1]*chrom_length)   

    if np.random.rand() < pm:  # if pm is greater than random number
        mask = claculate_mask(chrom_length, np.random.uniform(low=0.2, high=0.85))
        print("\nMask vector is:", mask)
        for i in range(chrom_length):
            if mask[i]==1:
                child_one[i] = parent_one[i]
            else:
                child_one[i] = parent_two[i]         

    else:  # if pm is less than random number then don't make any change
        child_one = deepcopy(parent_one)

    
    return child_one
