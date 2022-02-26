"""
https://leetcode-cn.com/problems/climbing-stairs/submissions/
思路:
    dp
    f(x) = f(x-1) + f(x-2)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n+1):
            for j in range(1, 3):
                if i >= j:
                    dp[i] += dp[i-j]

        return dp[-1]


