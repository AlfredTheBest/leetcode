"""
https://leetcode-cn.com/problems/regular-expression-matching/
思路:
    dp

f[i][j] 表示 S的前i个字符与p中的前j个字符是否能够匹配

p[j] is alpha
    f[i][j] = f[i-1][j-1] if s[i] == p[j]
    f[i][j] = False       if s[i] != p[j]

p[j] is *
    f[i][j] = f[i-1][j] or f[i][j-2] if s[i] == p[j-1]
    f[i][j] = f[i][j-2]              if s[i] != p[j-1]
"""

class Solution:

    def isMatch(self, s, p):
        m, n = len(s), len(p)

        def matches(i, j):
            if i == 0:
                return False

            if p[j-1] == '.':
                return True

            return s[i-1] == p[j-1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    f[i][j] |= f[i][j-2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i-1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i-1][j-1]

        return f[m][n]







