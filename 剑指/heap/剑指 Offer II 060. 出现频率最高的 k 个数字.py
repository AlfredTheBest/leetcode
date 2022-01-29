"""
https://leetcode-cn.com/problems/g5c51o/
思路:
    heapq
"""
from collections import *
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        minHeap = []

        for x, f in num_freq.items():
            if len(minHeap) == k:
                if minHeap[0][0] < f:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, (f, x))
            else:
                heapq.heappush(minHeap, (f, x))
        res  = []
        while minHeap:
            f, x = heapq.heappop(minHeap)
            res.append(x)
        return res


