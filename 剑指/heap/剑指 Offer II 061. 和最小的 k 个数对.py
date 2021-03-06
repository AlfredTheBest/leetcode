"""
https://leetcode-cn.com/problems/qn8gGX/
思路:
    heapq
"""

import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, [-(n1+n2),[n1,n2]])
                else:
                    if heap and heap[0][0] < -(n1+n2):
                        heapq.heappop(heap)
                        heapq.heappush(heap, [-(n1+n2), [n1, n2]])
                    else:
                        break
        return list(reversed([heapq.heappop(heap)[1] for _ in range(k) if heap]))

