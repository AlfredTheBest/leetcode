"""
https://leetcode-cn.com/problems/TVdhkn/
思路:
    backtracking
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = list()
        tmp = list()

        res.append([])

        def backtracking(nums, tmp, startIndex):
            if  startIndex == len(nums):
                return

            for i in range(startIndex, len(nums)):
                tmp.append(nums[i])
                res.append(list(tmp))
                backtracking(nums, tmp, i + 1)
                tmp.pop()

        backtracking(nums, tmp, 0)
        return res


