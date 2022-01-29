"""
https://leetcode-cn.com/problems/xoh6Oh/
给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%' 。
例如 15/2 7
思路:
    就是将b 扩大n倍 然后 a = a -n*b; c += n
    a / b = c
    cnt = 0
    如果 a>b
        b << 1
        cnt << 1
    直到不满足

    a = a-cnt * b
    c += cnt
"""


class Solution:
    def divide(self, a: int, b: int) -> int:
        ret = 0
        Int_MAX = 2**31 - 1
        flag = False if (a > 0 and b > 0) or (a < 0 and b < 0) else True
        a, b = abs(a), abs(b)
        def cal(a, b):
            cnt = 1
            while a > b << 1:
                b <<= 1
                cnt <<= 1
            return cnt, b

        ret = 0

        while a >= b:
            cnt, val = cal(a, b)
            ret += cnt
            a -= val
        ret = -ret if flag else ret
        return Int_MAX if ret > Int_MAX else ret






