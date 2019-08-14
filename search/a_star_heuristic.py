from queue import PriorityQueue


vertex = {
	'S': ['A', 'D'],
	'A': ['S', 'D', 'B'],
	'B': ['A', 'C', 'E'],
	'C': ['B'],
	'D': ['S', 'A', 'E'],
	'E': ['D', 'B', 'F'],
	'F': ['E', 'G'],
	'G': ['F']
}

weight = {
	'SA': 6,
	'SD': 3,
	'AS': 6,
	'AD': 5,
	'AB': 5,
	'BA': 5,
	'BC': 4,
	'BE': 5,
	'CB': 4,
	'DS': 3,
	'DA': 5,
	'DE': 2,
	'ED': 2,
	'EB': 5,
	'EF': 4,
	'FE': 4,
	'FG': 3,
	'GF': 3
}

heuristic = {
	'S': 12,
	'A': 8,
	'D': 9,
	'B': 7,
	'C': 5,
	'E': 4,
	'F': 2,
	'G': 0
}


def a_star(graph, start, goal):
	queue = PriorityQueue()
	queue.put(start, 0)
	visited = {}
	cost_so_far = {}
	visited[start] = None
	cost_so_far[start] = 0

	if start not in graph:
		raise TypeError('{} not found in graph!'.format(start))
		exit()
	if goal not in graph:
		raise TypeError('{} not found in graph!'.format(goal))
		exit()

	while not queue.empty():
		current = queue.get()

		if current == goal:
			break

		for neighbor in vertex[current]:
			new_cost = cost_so_far[current] + weight[current+neighbor]
			if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
				cost_so_far[neighbor] = new_cost
				priority = new_cost + heuristic[current]
				queue.put(neighbor, priority)
				visited[neighbor] = current

	return visited, cost_so_far[goal]


def reconstruct_path(visited, start, goal):
	current = goal
	path = []
	print(visited)
	while current != start:
		path.append(current)
		current = visited[current]
	path.append(start)
	path.reverse()
	return path


visited, cost = a_star(vertex, 'S', 'G')
path = reconstruct_path(visited, 'S', 'G')

print("Path for A* is: {} with cost of {}".format(path, cost))