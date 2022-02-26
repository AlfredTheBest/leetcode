"""
https://leetcode-cn.com/problems/IlPe0q/
https://leetcode-cn.com/problems/IlPe0q/solution/san-jiao-xing-zhong-zui-xiao-lu-jing-zhi-srun/
 思路:
    dp

        f[i][j] 代表 第i行第j列的值

        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]

        第一列  f[i][0] = f[i-1][0] + triangle[i][0]
        最后一列 f[i][i] = f[i - 1][i - 1] + triangle[i][i]
        其他 f[i][i] = min(f[i-1][j-1], f[i-1][j]) + triangle[i][j]

        return min(n-1)
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]

        return min(f[n - 1])



