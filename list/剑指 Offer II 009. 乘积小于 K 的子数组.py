"""
https://leetcode-cn.com/problems/ZVAVXX/

思路:
    双指针滑动题
        如果 下标left到right相乘小于 k 则有 right - left + 1个字集小于k
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

