#https://leetcode-cn.com/problems/longest-palindromic-substring/
#https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0005.%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.md
# 注意python的数组边界 前开后闭


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        maxlength = 0
        left = 0
        right = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[j] == s[i]:
                    if j - i <= 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                if dp[i][j] and j - i + 1 > maxlength:
                    maxlength = j - i + 1
                    left = i
                    right = j
        return s[left:right + 1]





