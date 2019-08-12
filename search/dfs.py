"""
######################### Algorithm #####################

1. Put the starting node on stack
2. If the stack is empty return FAILURE and STOP
3. If the first element on the stack is the GOAL node then return SUCCESS otherwise
4. Remove and expand the first element and place the children at the front of the stack
5. Return to step 2

"""

# undirected graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['E']
}

# # #directed graph
# graph = {
#     'A': ['B', 'C', 'D'],
#     'B': ['E'],
#     'C': ['D', 'F', 'G'],
#     'D': ['E'],
#     'E': ['G'],
#     'F': ['G'],
#     'G': []
# }


def dfs(graph, start, goal):
    visited = []
    stack = [start]
    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if not neighbor in visited:
                stack.append(neighbor)
        visited.append(current)
        if current == goal:
            break
    return visited


print(dfs(graph, 'A', 'E'))

# graph = {'S': set(['A', 'B', 'C']),
#          'A': set(['D', 'E', 'S']),
#          'D': set(['A']),
#          'E': set(['A']),
#          'B': set(['F', 'S']),
#          'F': set(['B']),
#          'C': set(['H', 'I', 'S']),
#          'H': set(['C']),
#          'I': set(['J', 'K']),
#          'J': set(['G', 'L']),
#          'G': set(['J']),
#          'L': set(['J']),
#          'K': set(['I'])}


# print(dfs(graph, 'S', 'G'))
