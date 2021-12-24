"""
https://leetcode-cn.com/problems/w3tCBm/

最高有效位:
    对于正整数x， 如果y是2的整数次幂 则 y只有最高位1，其他都为0
    那可以理解他都为0 只是最高位是1
    dp function: dp[i] = dp[i-high_bit] + 1
"""

class Solution:
    def countBits(self, n):
        bits = [0]
        high_bit = 0
        for i in range(1, n + 1):
            if i & (i - 1):
                high_bit = i
            bits.append(bits[i - high_bit] + 1)
        return bits