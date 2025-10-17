class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxarea = [0]

        def getNeighbors(x,y):
            neighbors = []
            if x+1<m:
                neighbors.append((x+1,y))
            if x-1>=0:
                neighbors.append((x-1,y))
            if y+1<n:
                neighbors.append((x,y+1))
            if y-1>=0:
                neighbors.append((x,y-1))
            return neighbors
        
        def bfs(row, col):
            q = deque([(row, col)])
            area = 1
            while q:
                nodex,nodey = q.popleft()
                grid[nodex][nodey] = 0
                for neighborx,neighbory in getNeighbors(nodex, nodey):
                    if grid[neighborx][neighbory] == 1:
                        grid[neighborx][neighbory] = 0
                        q.append((neighborx, neighbory))
                        area+=1
                        
            return area
        

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    area = bfs(row, col)
                    maxarea[0] = max(maxarea[0], area)
        return maxarea[0]
