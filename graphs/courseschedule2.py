class Solution:
  ## BFS cannot be used to find a cycle in a directed graph
  ## In DFS we need to find back edges to detect a cycle.
  ## A backedge can be detected by having a departure time array. 
  ## If the node is already visited we check if the node has no departure time set. 
  ## If it is not set that means we have a backedge and a cycle
  ## Adding an array to save the node before we exit will also give us the order
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        visited = [-1]* numCourses
        departure = [-1]*numCourses
        order = []

        for u,v in prerequisites:
            adjList[u].append(v)

        def dfs(source):
            visited[source] = 1
            for course in adjList[source]:
                if visited[course] == -1:
                    if dfs(course):
                        return True
                else:
                    if departure[course] == -1:
                        return True
            departure[source] +=1
            order.append(source)
            return False
        
        for course in range(numCourses):
            if visited[course] == -1:
                if dfs(course):
                    return []
        return order
        
