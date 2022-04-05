import random, tour, util

#mutate module holds the mutation operators
#util holds helper functions


#order crossover handles the selectino of the crossover point
#and performs the order crossover operation
def orderCrossover (parent_1, parent_2, NUM_CITIES):
    #get cross points and values for crossover/shifting
    first_point = random.randrange(1,NUM_CITIES-1)
    second_point = random.randrange(first_point+1, NUM_CITIES)
    parent_1_tour = parent_1.getTour()
    parent_2_tour = parent_2.getTour()
    child_1, child_2 = [None]*NUM_CITIES,[None]*NUM_CITIES

    
    #test begins here
    parent_1_tour = [0,7,4,5,8,9,6,2,3,1]
    parent_2_tour = [0,2,7,4,6,3,8,1,5,9]
    first_point = 4
    second_point = 7
    print("\nParent 1 is: ", parent_1_tour)
    print("Parent 2 is: ", parent_2_tour)
    print("\nCrossover point is between ", first_point, "and ", second_point)    
    #test ends here
    
    
    #return children in appropriate order
    for i in range(first_point,second_point):
        child_1[i] = parent_1_tour[i]
        child_2[i] = parent_2_tour[i]
    child_index = second_point
    parent_index = second_point

    #populate tour for child_1 after crossover
    for i in range(NUM_CITIES):
        if parent_2_tour[parent_index] not in child_1:
            child_1[child_index] = parent_2_tour[parent_index]
            child_index = util.getCrossoverIndex(child_index, NUM_CITIES)
        parent_index = util.getCrossoverIndex(parent_index, NUM_CITIES)
    child_index = second_point
    parent_index = second_point

    #populate tour for child_2 after crossover
    for i in range(NUM_CITIES):
        if parent_1_tour[parent_index] not in child_2:
            child_2[child_index] = parent_1_tour[parent_index]
            child_index = util.getCrossoverIndex(child_index, NUM_CITIES)
        parent_index = util.getCrossoverIndex(parent_index, NUM_CITIES)
    child_1[0], child_2[0] = 0, 0
    print (child_1,"\n", child_2)
    
    return child_1, child_2