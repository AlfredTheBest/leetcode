"""
https://leetcode-cn.com/problems/B1IidL/
思路: bi-search

"""
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid-1] < arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return mid


