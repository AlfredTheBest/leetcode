"""
https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode-solution-tuvc/
 思路:
    dp 算出 左右边最大值
    stack 单调递减栈储存可能储水的柱子
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currHeight * currWidth

            stack.append(i)

        return ans




class Solution_dp:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)

        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])

        rightMax = [0] * (n - 1) + [height[n-1]]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans

