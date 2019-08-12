"""
################## Algorithm ###############

1. Put the starting node on the queue
2. If the queue is empty then return FAILURE and STOP
3. If the first element on the queue is goal node then return SUCCESS
4. Otherwise, remove and expand the first element from the queue and place all the children at the end of the queue
5. Return to step 2

"""

graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D', 'E', 'S'],
    'D': ['A'],
    'E': ['A'],
    'B': ['F', 'S'],
    'F': ['B'],
    'C': ['H', 'I', 'S'],
    'H': ['C'],
    'I': ['J', 'K'],
    'J': ['G', 'L'],
    'G': ['J'],
    'L': ['J'],
    'K': ['I']
}



def bfs(graph, start, goal):
    visited = []
    queue = [start]
    while queue:
        print("Visited: ", visited)
        print("Queue: ",queue)
        current = queue.pop()
        for neighbor in graph[current]:
            if not neighbor in visited:
                queue.insert(0,neighbor) #list.insert(index, element)
        visited.append(current)
        if current == goal:
            break
    return visited

print(bfs(graph, 'S', 'J'))


