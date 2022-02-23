"""
https://leetcode-cn.com/problems/jBjn9C/
思路:
    heapq
"""
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = []
        for ii in nums:
            self.add(ii)


    def add(self, val: int) -> int:
        heapq.heappush(self.arr,val)
        if len(self.arr) > self.k:
            heapq.heappop(self.arr)
        return self.arr[0]


