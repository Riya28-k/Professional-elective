from collections import deque

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node] - visited)

# Take user input for graph
graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node name {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = set(neighbors)

start_node = input("Enter starting node: ")

print("BFS Traversal:")
bfs(graph, start_node)
