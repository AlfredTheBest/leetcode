"""
https://leetcode-cn.com/problems/nZZqjQ/
思路:
    bi-search
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(speed):
            return sum(ceil(p / speed) for p in piles) <= h

        l = 1
        r = max(piles)

        while l  < r:
            mid = (l + r) // 2
            if check(mid) == True:
                r = mid
            else:
                l = mid + 1

        return l





