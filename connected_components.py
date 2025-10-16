class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        visited = [-1]*n

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def bfs(source):
            q = deque([source])
            while q:
                node = q.popleft()
                visited[node] = 1
                for neighbor in adjList[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        q.append(neighbor)
        
        count = 0
        for v in range(n):
            if visited[v] == -1:
                count+=1
                bfs(v)
        return count

                
            
        
