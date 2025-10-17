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
                    



        
