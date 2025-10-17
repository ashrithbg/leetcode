## Checking for bipartiteness means in case of DFS finding cycles with odd length. 
## So we will have a distance array. We add one to the neighbor's distance as we discover it.
## In case of BFS in undirected graphs only cross edges lead to cycles and even amongst cross edges only the ones which are at the same level.
## So checking for equality in distance between neighbor and node will confirm if it has an odd length cycle(i.e cross edge at the same level)


## If we use DFS we need to find back edges. 
## We have a color array array with all values set to false. When we visit a neighbor we will invert its color from that of the parent
## If we find that we already visited the vertex i.e presence of a cycle we compare the colors and if they are the same that means we found a back egde of odd length

#BFS implementation: track dist (or color = dist % 2). If you see an edge (u, v) with dist[u] == dist[v], return False.

#DFS implementation: track color in {0,1}; if you see an edge to an already colored vertex with the same color, return False.

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        visited = [-1]*n
        distance = [-1]*n
        color = [False]*n

        def dfs(source):
            visited[source]=1
            for neighbor in graph[source]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    color[neighbor] = not color[source]
                    if dfs(neighbor):
                        return True
                else:
                    if color[neighbor] == color[source]:
                        return True
            return False

        def bfs(source):
            q = deque([source])
            distance[source] = 0
            while q:
                node = q.popleft()
                visited[node] = 1
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        distance[neighbor] = distance[node]+1
                        q.append(neighbor)
                    else:
                        if distance[neighbor] == distance[node]:
                            return True
            return False

        for v in range(n):
            if visited[v] == -1:
                if dfs(v):
                    return False
        return True
                    



        
