"""
https://leetcode-cn.com/problems/jJ0w9p/
思路:
    bi-search
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 <= x and (mid + 1) ** 2 > x:
                return mid
            elif mid ** 2 < x:
                left = mid + 1
            elif mid ** 2 > x:
                right = mid - 1








