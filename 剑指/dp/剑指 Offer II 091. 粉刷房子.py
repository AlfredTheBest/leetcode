"""
https://leetcode-cn.com/problems/JEj789/
思路:
    dp

    dp[i][j] i 代表第几个房子 j 代表 使用第几个颜色

    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    return(min(dp[-1]))
"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        if len(costs) == 1: return min(dp)

        for i in range(1, len(costs)):
            tmp = [0] * 3
            tmp[0] = costs[i][0] + min(dp[1], dp[2])
            tmp[1] = costs[i][1] + min(dp[0], dp[2])
            tmp[2] = costs[i][2] + min(dp[0], dp[1])
            dp = tmp

        return min(dp)






