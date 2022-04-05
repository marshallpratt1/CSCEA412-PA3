#####################################################################
#tour class stores all attributes of a tour
#a tour will be made in the initial seeding of the first generation
#new tours will be made as offspring of parent tours selected for repropduction
#####################################################################

class Tour:
    def __init__(self):
        self.tour = []
        self.cost = None
        self.parent = None
        generation = None
        

    def setTour (self, value_list):
        for i in value_list:
            self.tour.append(i)

    def setGeneration (self, gen):
        self.generation = gen

    def setCost (self, val):
        self.cost = val

    def incrementGeneration(self):
        self.generation+=1

    def getTour (self):
        return self.tour

    def getGeneration(self):
        return self.generation

    def getCost (self):
        return self.cost