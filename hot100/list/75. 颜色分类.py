"""
https://leetcode-cn.com/problems/sort-colors/
思路:
    双指针
"""
class Solution:
    def sortColors(self, nums):
        n = len(nums)
        p0, p1 = 0, n - 1
        i = 0

        while i <= p1:
            while i <= p1 and nums[i] == 2:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 -= 1
            while i >= p0 and nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1

            i += 1







