"""
https://leetcode-cn.com/problems/uUsW3B/
思路:
    backtracking
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrace(idx):

            if len(path) == k:
                res.append(path[:])
                return

            if idx == n + 1: return

            backtrace(idx + 1)

            path.append(idx)
            backtrace(idx + 1)
            path.pop()

        backtrace(1)
        return res


