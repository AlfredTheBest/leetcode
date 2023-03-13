"""
https://leetcode-cn.com/problems/cyJERH/
思路:
    dp
"""

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = [[0,1] if s[0] == '0' else [1,0]]

        for i in range(1, len(s)):
            dp.append([dp[-1][0] + 1, min(dp[-1][1], dp[-1][0])] if s[i] == '1'
                      else [dp[-1][0], dp[-1][1]+1])

        return min(dp[-1])




class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = []
        if s[0] == '1':
            dp.append([1, 0])
        else:
            dp.append([0, 1])
        
        for i in range(1, len(s)):
            if s[i] == '1':
                dp.append([dp[-1][0] + 1, min(dp[-1][1], dp[-1][0])])
            else:
                dp.append([dp[-1][0], dp[-1][1] + 1])
        
        return min(dp[-1])
