class Solution:
  ## BFS cannot be used to find a cycle in a directed graph
  ## In DFS we need to find back edges to detect a cycle.
  ## A backedge can be detected by having a departure time array. 
  ## If the node is already visited we check if the node has no departure time set. 
  ## If it is not set that means we have a backedge and a cycle
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = [[] for _ in range(numCourses)]
        visited = [-1]* numCourses

      
        departure = [-1]*numCourses

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
            return False
        
        for course in range(numCourses):
            if visited[course] == -1:
                if dfs(course):
                    return False
        return True

        
