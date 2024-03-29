"""
https://leetcode-cn.com/problems/0ynMMM/
思路:
    栈
    栈其实可以有方向性
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(-1, 0)]
        ans = 0
        for i, v in enumerate(heights + [0]):
            lasti = i

            while v < stack[-1][1]:
                lasti, lastv = stack.pop()
                ans = max(ans, lastv * (i - lasti))

            if v > stack[-1][1]:
                stack.append([lasti, v])
        return ans






class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[(-1,-1)]
        H=heights+[0]
        ans=0
        for i,h in enumerate(H):
            while stack[-1][1] > h:
                _, oh = stack.pop()
                s = (i-stack[-1][0]-1)*oh
                ans = max(ans, s)
            stack.append((i, h))
        return ans

        

