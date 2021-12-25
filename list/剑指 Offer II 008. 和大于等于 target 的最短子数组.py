"""
https://leetcode-cn.com/problems/2VG8Kg/


思路:
    前缀和 + 二分查找

"""
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        def binary_search(s, k):
            # 在s中找大于等于k的第一个元素
            low  = 0
            high = len(s) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if s[mid] < k:
                    low = mid + 1
                else:
                    if mid == 0 or s[mid - 1] < k:
                        return mid
                    else:
                        high = mid - 1

        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = binary_search(sums, target)

            if bound and bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans













