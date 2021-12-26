"""
https://leetcode-cn.com/problems/a7VOhD/
https://leetcode-cn.com/problems/a7VOhD/solution/cpython3java-1dp-2zhong-xin-kuo-san-by-h-ad5t/
思路:
    dp
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        res = n

        for l in range(n-1, -1, -1):
            for r in range(l+1, n):
                if s[l] == s[r]:
                    if r - l == 1:
                        dp[l][r] = True
                        res += 1
                    else:
                        if dp[l+1][r-1] == True:
                            dp[l][r] = True
                            res += 1
        return res