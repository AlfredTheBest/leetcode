"""
https://leetcode-cn.com/problems/7WqeDu/

思路:
    1. 桶
"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket = {}
        for i in range(len(nums)):
            b = nums[i]//(t+1)#b是桶的序号，具有相同num//t+1的num值会分到同一个桶里，
            if b in bucket: return True
            if b-1 in bucket and abs(bucket[b-1]-nums[i])<=t: return True
            if b+1 in bucket and abs(bucket[b+1]-nums[i])<=t: return True
            bucket[b] = nums[i]

            if i >= k: bucket.pop(nums[i-k] // (t+1))

        return False











