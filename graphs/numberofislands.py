class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        islands = 0

        def getNeighbor(x,y):
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
            while q:
                noder,nodec = q.popleft()
                grid[noder][nodec] = '0'
                for neighborp,neighborq in getNeighbor(noder,nodec):
                    if grid[neighborp][neighborq] == '1':
                        grid[neighborp][neighborq] = '0'
                        q.append((neighborp, neighborq))


        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    islands+=1
                    bfs(row,col)
        return islands
        

        
