"""
https://leetcode-cn.com/problems/longest-valid-parentheses/
思路:
    stack
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) > 0:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res



