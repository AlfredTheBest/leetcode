"""
https://leetcode-cn.com/problems/xx4gT2/
思路:
    heapq sort
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-ele for ele in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)

