"""
https://leetcode-cn.com/problems/2VG8Kg/
https://leetcode-cn.com/problems/2VG8Kg/solution/he-da-yu-deng-yu-target-de-zui-duan-zi-s-ixef/

思路:
    滑动窗口

"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans








