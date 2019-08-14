from queue import PriorityQueue


vertex = {
	'A': ['B', 'C', 'D'],
	'B': ['E'],
	'C': ['D', 'F', 'G'],
	'D': ['E'],
	'E': ['G'],
	'F': ['G'],
	'G': []
}

weight = {
	'AB': 5,
	'AD': 3,
	'AC': 4,
	'CD': 1,
	'CF': 2,
	'CG': 3,
	'DE': 4,
	'DA': 7,
	'BE': 3,
	'EG': 2,
	'FG': 0.5
}

loc = {
	'A': (0, 0),
	'B': (0, 4),
	'C': (3, 0),
	'D': (2, 2),
	'E': (3, 4),
	'F': (5, 2),
	'G': (5, 4)
}


def heuristic(a, b):
	(x1, y1) = a
	(x2, y2) = b
	return abs(x1-x2) + abs(y1-y2)

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
				priority = new_cost + heuristic(loc[goal], loc[neighbor])
				# print(neighbor, heuristic(loc[goal], loc[neighbor]))
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


visited, cost = a_star(vertex, 'A', 'G')
path = reconstruct_path(visited, 'A', 'G')

print("Path for A* is: {} with cost of {}".format(path, cost))