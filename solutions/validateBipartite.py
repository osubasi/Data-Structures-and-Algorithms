# Omer Subasi

def validateBipartite(graph):
    def dfs(node, color, graph, colors):
        colors[node] = color
        for neighbor in graph[node]:
            if colors[neighbor] == color:
                return False
            if colors[neighbor] == 0 and not dfs(neighbor, -color, graph, colors):
                return False 
        return True    

    colors = [0] * len(graph)
    for i in range(len(graph)):
        if colors[i] == 0 and not dfs(i, 1, graph, colors):
            return False
    return True
