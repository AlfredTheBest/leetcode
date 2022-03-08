"""
https://leetcode-cn.com/problems/a7VOhD/
https://leetcode-cn.com/problems/a7VOhD/solution/jian-zhi-offer-ii-020-hui-wen-zi-zi-fu-c-690y/
思路:
    dp
注意嵌套循环

"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        length = len(s)
        #动态规划
        dp = [[0]* length for _ in range(length)]
        for i in range(length-1, -1, -1):   #dp[i][j]由dp[i+1][j-1]决定，所以i要从大到小计算
            for j in range(i, length):    #保证i<=j
                if s[i] != s[j]:
                    continue
                dp[i][j] = j-i<=2 or dp[i+1][j-1]
                if dp[i][j]:
                    count+=1
        return count
