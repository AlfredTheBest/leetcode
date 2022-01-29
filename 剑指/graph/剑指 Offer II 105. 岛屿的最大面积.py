"""
https://leetcode-cn.com/problems/ZL6zAn/
思路
    dfs
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            res = 1
            grid[i][j] = 0
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    res += dfs(x, y)
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans