# So, this is DFS, Depth First Search.

input_graph = {
    "A": set(["B", "C"]),
    "B": set(["A", "D", "E"]),
    "C": set(["A", "F"]),
    "D": set(["B"]),
    "E": set(["B", "F"]),
    "F": set(["C", "E"]),
}

# Understand this code and concepts behind this code, in very much details.

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            # Recursion is happening, here.
            dfs(graph, n, visited)
                return visited
            # Why here, 'A" is in the inputs?
            visited = dfs(input_graph, "A", [])
            print(visited)