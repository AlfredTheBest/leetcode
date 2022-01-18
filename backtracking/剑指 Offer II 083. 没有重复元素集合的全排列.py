"""
https://leetcode-cn.com/problems/VvJkup/
思路:
    backtracking
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking(path, nums):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtracking(path, nums)
                    path.pop()

        backtracking(path, nums)
        return res











