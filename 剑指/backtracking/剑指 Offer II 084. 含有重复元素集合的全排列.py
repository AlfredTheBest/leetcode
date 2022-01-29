"""
https://leetcode-cn.com/problems/7p8L0Z/
思路:
    backtracking
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, usedlist):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if usedlist[i] == True:
                    continue

                if i > 0 and nums[i - 1] == nums[i] and usedlist[i-1] == False:
                    continue

                path.append(nums[i])
                usedlist[i] = True
                backtracking(nums, usedlist)
                usedlist[i] = False
                path.pop()

        res = []
        path = []
        usedlist = [False] * len(nums)
        nums.sort()
        backtracking(nums, usedlist)
        return res

