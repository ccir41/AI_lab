# credit: https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35

"""
					Algorithm

	1. Initialize the population and number of generation
	2. Repeat step 3 to 8 until the number of generation is meet
	3. Evaluate the fitness value of each chromosome by using objective function
	4. Select the parent chromosomes
	5. Perform crossover
	6. Perform mutation
	7. Generate new offspring 
	8. Display the best chromosome which is the solution of the problem 

"""



import numpy as np
import random, operator
import matplotlib.pyplot as plt


cityList = [(92,118), (9,173), (20,189), (112,198), (107,168), (105,134), (118,137), (125,146)] # [city1, city2, ...]

# to calculate distance between two cities
def distance(fromCity, toCity): # (city1, city2)
	x1,y1 = fromCity
	x2,y2 = toCity
	x_dis = abs(x1 - x2)
	y_dis = abs(y1 - y2)
	distance = np.sqrt(x_dis**2 + y_dis**2)
	return distance

# to calculate total distance of a route
def routeDistance(route): # example: route = [(9,173), (20,189), (92,118), (112,198), (105,134), (107,168), (125,146), (118,137)]
	pathDistance = 0
	for i in range(0, len(route)): # length = 8
		fromCity = route[i] # if i = 0 then (9, 173)
		toCity = None
		if i+1 < len(route): # 1 < 8
			toCity = route[i+1] # (20, 189)
		else: # if last in route
			toCity = route[0] # (9, 173)
		pathDistance += distance(fromCity, toCity)
	return pathDistance


# create a random route from given city lists
def createRoute(cityList): # cityList = [(92,118), (9,173), (20,189), (112,198), (107,168), (105,134), (118,137), (125,146)]
	route = random.sample(cityList, len(cityList)) # example: route = [(9,173), (20,189), (92,118), (112,198), (105,134), (107,168), (125,146), (118,137)]
	return route


# calculate fitness of given route
def routeFitness(route):
	fitness = 1.0 / float(routeDistance(route)) # we want to minimize distance i.e. maxfitness is inverse of distance
	return fitness

# collection of routes
def initialPopulation(popSize, cityList):
	population = []
	for i in range(0, popSize):
		population.append(createRoute(cityList))
	return population

# sort routes according to their fitness
def rankRoutes(population):
	fitnessResults = {}
	for i in range(0, len(population)):
		fitnessResults[i] = routeFitness(population[i]) # (index, fitness) example: [(0, 0.012), (1, 0.010), (2, 0.005), ...]
	return sorted(fitnessResults.items(), key=operator.itemgetter(1), reverse = True) # custom sort with key parameter i.e sort according to fitness value [(0, 0.012), (1, 0.010),..]

# select routes with high fitness value
def selection(popRanked, eliteSize): # eliteSize is the number of good individual that is to be selected in next generations
	selectionResults = []
	for i in range(0, eliteSize):
		selectionResults.append(popRanked[i][0]) # getting index of those population that are fittest
	return selectionResults

# collect parent for mating
def matingPool(population, selectionResults):
	matingpool = []
	for i in range(0, len(selectionResults)):
		index = selectionResults[i]
		matingpool.append(population[index])
	return matingpool

# crossover
def breed(parent1, parent2):
	child = []
	childP1 = []
	childP2 = []
	for i in range(3, 5):
		childP1.append(parent1[i])
	childP2 = [item for item in parent2 if item not in childP1] # there should not be any duplicate cities in a cityList
	child = childP1 + childP2
	return child

# crossover in population
def breedPopulation(matingpool, eliteSize):
	children = []
	pool = random.sample(matingpool, len(matingpool))

	for i in range(0, eliteSize):
		children.append(matingpool[i])

	for i in range(0, 8):
		child = breed(pool[i], pool[len(matingpool)-i-1])
		children.append(child)
	return children

# mutation in individual
def mutate(individual, mutationRate):
	for swapped in range(len(individual)):
		if (random.random() < mutationRate):
			swapWidth = int(random.random()*len(individual))

			city1 = individual[swapped]
			city2 = individual[swapWidth]

			individual[swapped] = city2
			individual[swapWidth] = city1

	return individual

# mutation in population
def mutatePopulation(population, mutationRate):
	mutatedPop = []
	for ind in range(0, len(population)):
		mutatedInd = mutate(population[ind], mutationRate)
		mutatedPop.append(mutatedInd)
	return mutatedPop

# iteration upto predifined number of generations
def nextGeneration(currentGen, eliteSize, mutationRate):
	popRanked = rankRoutes(currentGen)
	selectionResults = selection(popRanked, eliteSize)
	matingpool = matingPool(currentGen, selectionResults)
	children = breedPopulation(matingpool, eliteSize)
	nextGeneration = mutatePopulation(children, mutationRate)
	return nextGeneration

# Algorithm
def geneticAlgorith(population, popSize, eliteSize, mutationRate, generations):
	pop = initialPopulation(popSize, population)
	print("Initial distance is: {}".format(1 / rankRoutes(pop)[0][1]))

	for i in range(0, generations):
		pop = nextGeneration(pop, eliteSize, mutationRate)

	print("Final distance is: {}".format(1 / rankRoutes(pop)[0][1]))

	bestRouteIndex = rankRoutes(pop)[0][0]
	bestRoute = pop[bestRouteIndex]
	return bestRoute


best_path = geneticAlgorith(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
print("Optimum path is: {}".format(best_path))

# Plot Function
def geneticAlgorithmPlot(population, popSize, eliteSize, mutationRate, generations):
	pop = initialPopulation(popSize, population)
	progress = []
	progress.append(1/rankRoutes(pop)[0][1])

	for i in range(0, generations):
		pop = nextGeneration(pop, eliteSize, mutationRate)
		progress.append(1/rankRoutes(pop)[0][1])

	plt.plot(progress)
	plt.ylabel('Distance')
	plt.xlabel('Generations')
	plt.show()

geneticAlgorithmPlot(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
