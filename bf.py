graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
predecessors = [0]*len(graph.keys())
def bfs(graph, start, end):
    visited, queue = [], [start]
    path=[]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.extend(vertex)
        for child in graph[vertex]:
             if child not in visited:
                visited.extend(child)
                queue.extend(child)
                predecessors[ord(child)-65]=ord(vertex)-65
    current = end;
    while current != start:
        path.extend(current);
        current = chr(predecessors[ord(current)-65]+65)
    return path

v= bfs(graph,'A','F')
print(len(v)," ",v)

