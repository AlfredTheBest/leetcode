"""
https://leetcode-cn.com/problems/maximum-subarray/
思路:
    dp
    f[i] 指的是到i位置阿最大子序和
    f[i] = max(f[i-1] + nums[i], nums[i])
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        pre = 0
        n = len(nums)
        for i in range(n):
            pre = max(pre + nums[i], nums[i])
            ret = max(pre, ret)
        return ret





