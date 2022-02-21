"""
https://leetcode-cn.com/problems/longest-palindromic-substring/
思路:
    dp
    这是三个以上的
    P(i,j) = P(i+1, j-1)^(Si==Sj)
    两个以内
    P(i,i) = True
    P(i, i+1) = (Si == Si+1)
"""

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][j] = True

        for L in range(2, n + 1):
            for i in range(n):
                j = L + i - 1
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
                    
        return s[begin:begin + max_len]

















