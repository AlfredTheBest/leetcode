"""
https://leetcode-cn.com/problems/IY6buf/
思路:
    dp
    dp(i, j)代表 s1[i] s2[j] s3[i+j+1] 是 交织的

    dp(i, j) =
        s1[i] == s3[i+j+1] and dp(i-1, j) or
        s2[j] == s3[i+j+1] and dp(i, j-1)
    if i == -1: return s2[:j+1] == s3[:j+1]
    if j == -1: return s1[:i+1] == s3[:i+1]

    return dp(i, j)
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1,n2,n3=len(s1),len(s2),len(s3)
        if n1+n2!=n3: return False
        #动态规划
        #f(i,j)为True表示s1[0,i],s2[0,j]能交织成s3[0,i+j+1]
        #递推公式：
        #f(0,0) = s3 == s1[0]+s2[0] or s2[0]+s1[0]
        #最后一个元素来自s1 -> f(i,j) = f(i-1,j) and s1[i] == s3[i+j+1]
        #最后一个元素来自s2 -> f(i,j) = f(i,j-1) and s2[j] == s3[i+j+1]
        @cache
        def f(i,j):
            if i == -1: return s2[:j+1] == s3[:j+1]
            if j == -1: return s1[:i+1] == s3[:i+1]
            return s1[i]==s3[i+j+1] and f(i-1,j) or s2[j]==s3[i+j+1] and f(i,j-1)
        return f(n1-1,n2-1)








