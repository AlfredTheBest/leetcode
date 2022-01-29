"""
https://leetcode-cn.com/problems/dKk3P7/
思路:
    数组法
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or s == t:
            return False

        comp = [0] * 26

        for i in s:
            comp[ord(i) - 97] += 1

        for j in t:
            index = ord(j) - 97
            if comp[index] < 1:
                return False
            comp[index] -= 1
        return True
