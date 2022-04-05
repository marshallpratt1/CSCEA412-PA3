
from math import inf
from os import remove
import grid, util, sys, tour, mutate



#################################################
#
#This program solves the Traveling Salesperson problem 
#using Genetic Algortihms
#
#################################################

#set this to  desired generations
NUM_GENERATIONS = 1000
#set this to the desired population size
POPULATION_SIZE = 100
#set this to the desired number of cities
NUM_CITIES = 10
#Number of elites to carry over and worsts to get rid of
ELITE_SIZE, WORST_SIZE = 1, 1
#set the number of parents to select for breeding
NUM_PARENTS = 4
#stores the current population of tour objects
current_population = []
#stores the tours for replica checking
list_of_tours = []
#maps trip cost to tour object
cost_map = {}
#stores the top x of the tours for reproduction
best_tours = []
#stores the worst x of the tours for replacement
worst_tours = []
#this is the cost grid that we will use for all 12 runs
city_tour = grid.Grid(NUM_CITIES)
#run map stores a mapping of index to a run string for display purposes
run_map = {
    0: "Insert Mutation",
    1: "Swap Mutation",
    2: "Inversion Mutation",
    3: "Scramble Mutation"
}
insertMutChance = .2
swapMutChance = .2
invMutChance = .2
scramMutChance = .2


def main():
#mutation maps an index to a mutation operator
    print("Running")
    mutation_map = {
        0: util.insertMutation,
        1: util.swapMutation,
        2: util.inversionMutation,
        3: util.scrambleMutation
    }    
    #initialize variables for tours and starting lowest cost    
    best_run_cost = inf
    best_run_generation = None
    best_tour_cost = inf
    best_tour_generation = None

    #seed first generation and get initial best/worst cost values
    util.initialize(city_tour, current_population, cost_map, worst_tours, best_tours, list_of_tours, WORST_SIZE)
    

    print("\nWelcome to the 'Traveling Salesperson' route finding application\n")

    #outer loop runs four times (once for each mutation)
    for mutation in range (4):        
        print ("\nRunning ", run_map[mutation])
        #middle loop runs each mutation operator three time
        for run in range (3):
            print("\nThe starting best tour for run #", run, " of the ", run_map[mutation], " is: " )
            print("Cost: ", best_tours[0].getCost(), "   Generation: ", best_run_generation)
            #inner loop runs each attempt for the number of generations selected
            for i in range (NUM_GENERATIONS):
                #TODO!!! ensure that the population doesn't converge into a bunch of replicas
            
                #select parents for tournament selection        
                parents = util.getTournamentParents(current_population, NUM_PARENTS)                
                #perform crossover        
                children = util.breedCrossover(parents)                
                
                
                ########################################################################
                #perform additional mutations
                #TODO: handle/call the four different operators here
                #mutation operators can be called as outlined below:

                #Uncomment below to see the mutation

                if mutation_map[mutation] is mutation_map[0]:
                    children = mutation_map[mutation](children, insertMutChance)
                elif mutation_map[mutation] is mutation_map[1]:
                    children = mutation_map[mutation](children, swapMutChance)
                elif mutation_map[mutation] is mutation_map[2]:
                    #TODO Marshall Cherrier
                    children = mutation_map[mutation](children, invMutChance)
                elif mutation_map[mutation] is mutation_map[3]:
                    #TODO Marshall Cherrier
                    children = mutation_map[mutation](children, scramMutChance)


                ########################################################################                    
                
                
                #select the worst individuals for removal                
                util.getSacrifice(cost_map, current_population, list_of_tours, worst_tours)                           
                #fill and order this generation, make tour objects out of our children
                util.setChildren(children, current_population, cost_map, city_tour, list_of_tours, i+2)           
                util.getWorstTours(WORST_SIZE, worst_tours, cost_map)
                util.getBestTours(1, best_tours, cost_map)

                if best_tours[0].getCost() < best_run_cost:
                    best_run_cost = best_tours[0].getCost()
                    best_run_generation = best_tours[0].getGeneration()

                best_tours.clear()
            
            #display this runs results and 
            print("The best tour for run #", run, " of the ", run_map[mutation], " is: " )
            print("Cost: ", best_run_cost, "   Generation: ", best_run_generation)
            #reset variables for next run
            best_run_cost = inf
            best_run_generation = None
            util.reset(current_population, cost_map, best_tours, worst_tours, list_of_tours, city_tour, WORST_SIZE, ELITE_SIZE)
            

    print ("All done!")

if __name__=='__main__':
        main()