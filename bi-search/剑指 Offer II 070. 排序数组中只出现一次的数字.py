"""
https://leetcode-cn.com/problems/skFtm2/
思路:
    bi-search

"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            m = (l + r) // 2

            if m % 2 != 0:
                m = m - 1

            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m

        return nums[r]












