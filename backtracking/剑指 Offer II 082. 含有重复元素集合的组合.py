"""
https://leetcode-cn.com/problems/4sjJUc/
思路:
    backtracking
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrace(idx, t_val, path):
            if t_val == 0:
                self.res.append(path[:])
                return

            for i in range(idx, n):
                num = candidates[i]
                if num > t_val or (i > idx and num == candidates[i - 1]):
                    continue
                path.append(num)
                backtrace(i+1, t_val - num, path)
                path.pop()

        candidates.sort()
        n, self.res = len(candidates), []
        backtrace(0, target, [])
        return self.res








