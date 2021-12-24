"""
https://leetcode-cn.com/problems/JFETK5/

思路:
    循环
        计算当前 x 和 y 的无进位相加结果
        计算当前 x 和 y 的进位
"""

class Solution:
    def addBinary(self, a, b):
        x, y = int(a, 2), int(b, 2)
        while y:
            ans = x ^ y
            up = (x & y) << 1
            x, y = ans, up

        return bin(x)[2:]




















