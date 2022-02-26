"""
https://leetcode-cn.com/problems/qJnOS7/
思路:
    dp

    dp[i][j] 代表 text1[:i] 和 text2[:j] 最长公共子串

    dp[i][j]
        if text1[i-1] == text2[j-1]
            dp[i][j] = dp[i-1][j-1] + 1
        else
            dp[i][j] = max(dp[i-1][j], dp[i][j - 1])

    return dp[m][n]
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]









