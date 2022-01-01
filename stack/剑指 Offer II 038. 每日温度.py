"""
https://leetcode-cn.com/problems/iIQa4I/
https://leetcode-cn.com/problems/iIQa4I/solution/shua-chuan-jian-zhi-offer-day18-zhan-ii-mdv06/
思路:
    栈+list
"""
class Solution:
    def dailyTemperatures(self, temperatures):
        stack, ret = [], [0] * len(temperatures)
        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                index = stack.pop()
                ret[index] = i - index
            stack.append(i)
        return ret