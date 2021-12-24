class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtrack(nums):
            if len(path) == len(nums):
                return res.append(path[:])
            for i in range(0, len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(nums)
                path.pop()
        backtrack(nums)
        return res