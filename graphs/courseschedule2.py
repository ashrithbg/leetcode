class Solution:
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
        
