"""
https://leetcode-cn.com/problems/8Zf90G/
https://leetcode-cn.com/problems/8Zf90G/solution/shua-chuan-jian-zhi-offer-day10-zi-fu-ch-c9f1/
思路:
    使用栈
"""

class Solution:
    def evalRPN(self,tokens):

        stack = []

        calc =  {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),
        }

        for i in tokens:
            if i in calc:
                num2, num1 = stack.pop(), stack.pop()
                stack.append(calc[i](num1, num2))
            else:
                stack.append(int(i))

        return stack[0]
























