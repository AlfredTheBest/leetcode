"""
https://leetcode-cn.com/problems/uUsW3B/
思路:
    backtracking
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        tmp = []
        
        def backtrack(index):
            if len(tmp) == k:
                ret.append(tmp[:])
                return
            
            for i in range(index, n+1):
                tmp.append(i)
                backtrack(i + 1)
                tmp.pop()
        
        backtrack(1)
        return ret


