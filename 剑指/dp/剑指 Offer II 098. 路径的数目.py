"""
https://leetcode-cn.com/problems/2AoeFn/
思路:
    dp

    dp[i][j] 代表到 i,j 有多少路径

    dp[i][j] = dp[i-1][j] + dp[i][j-1]

    dp[0][i] = 1
    dp[i][0] = 1

    dp[m-1][n-1]
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1

        for i in range(n):
            dp[0][i] = 1

        if dp[m-1][n-1] != 0: return 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m-1][n-1]



