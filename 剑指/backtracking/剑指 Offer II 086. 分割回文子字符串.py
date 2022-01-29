"""
https://leetcode-cn.com/problems/M99OJA/
思路:
    backtrack
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        trace = []
        n = len(s)

        def backTrack(start):
            if start == n:
                res.append(trace[:])

            for i in range(start, n + 1):
                cur = s[start:i]
                if cur == cur[::-1] and cur != '':
                    trace.append(cur)
                    backTrack(i)
                    trace.pop()

        backTrack(0)
        return res




