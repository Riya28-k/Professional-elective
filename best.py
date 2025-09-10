from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))  # (priority, node)

    while not pq.empty():
        _, current = pq.get()
        if current in visited:
            continue
        print(current, end=" ")

        if current == goal:
            print("\nGoal reached!")
            return

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

# --- User Input Section ---
graph = {}
nodes = int(input("Enter number of nodes: "))

print("\nEnter node names:")
node_list = [input(f"Node {i+1}: ") for i in range(nodes)]

# Build graph
for node in node_list:
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

# Heuristic values
heuristic = {}
print("\nEnter heuristic values:")
for node in node_list:
    heuristic[node] = int(input(f"Heuristic value for {node}: "))

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

print("\nBest First Search Path:")
best_first_search(graph, start, goal, heuristic)
