"""
https://leetcode-cn.com/problems/omKAoA/

思路:
    dp
    dp[i] 从 0 到 i 最小可分割次数
    dp[i] = min(d[j]+1, dp[i]) if isPalindrome(s[j:i])
    return dp[-1]
"""

class Solution_v1:
    def minCut(self, s: str) -> int:
        isPalindorme=lambda s: s==s[::-1]
        n = len(s)
        dp = [n-1] * (n + 1)
        dp[0] = -1
        for i in range(1, n + 1):
            for j in range(i):
                if isPalindorme(s[j:i]): dp[i]=min(dp[j]+1,dp[i])
        return dp[-1]


class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)

        isvalid = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            isvalid[i][i] = True
            if i + 1 < n:
                isvalid[i][i+1] = s[i] == s[i+1]
            for j in range(i+2, n):
                isvalid[i][j] = isvalid[i+1][j-1] and s[i] == s[j]

        dp = [n] * n
        for i in range(n):
            if isvalid[0][i]:
                dp[i] = 0
            else:
                dp[i] = min(dp[j] + 1 for j in range(i) if isvalid[j+1][i])

        return dp[-1]






