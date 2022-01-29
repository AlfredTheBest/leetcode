"""
https://leetcode-cn.com/problems/569nqc/
思路:
    环形问题要不链接要不拍平 这个是不一个拍平
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mins = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        mins.append(mins[0] + 24 * 60)
        res = mins[-1]
        for i in range(1, len(mins)):
            res = min(res, mins[i] - mins[i - 1])
        return res
