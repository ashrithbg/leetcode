class Solution:
    ## A tree is a graph with no cycles and only one connected component.
###Make sure to check the count of connected components alongwith checking if the neighbor is already visited(and is not a parent)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for _ in range(n)]

        visited = [-1]*n
        parent = [-1]*n

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
                        parent[neighbor] = node
                        q.append(neighbor)
                    else:
                        if neighbor!=parent[node]:
                            return True

            return False
        count = 0
        for v in range(n):
            if visited[v] == -1:
                count+=1
                if bfs(v) or count>1:
                    return False
        # if count >1:
        #     return False
        return True




        
        
