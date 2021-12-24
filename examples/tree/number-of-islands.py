class Solution:

    def depthSearch(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        self.depthSearch(grid, i-1, j)
        self.depthSearch(grid, i+1, j)
        self.depthSearch(grid, i, j-1)
        self.depthSearch(grid, i, j+1)
        

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        w,h = len(grid[0]), len(grid)
        cnt = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    self.depthSearch(grid, i, j)
                    cnt += 1
        
        return cnt
