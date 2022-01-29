"""
https://leetcode-cn.com/problems/B1IidL/
思路: bi-search

"""
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right, ans = 1, n-1, 0

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans










