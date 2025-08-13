# DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Take user input for graph
graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node name {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbors

start_node = input("Enter starting node: ")

print("DFS Traversal:")
dfs(graph, start_node)
