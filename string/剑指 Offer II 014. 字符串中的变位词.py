"""
https://leetcode-cn.com/problems/MPnaiL/
思路:
    双指针问题
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1, arr2, lg = [0] * 26, [0] * 26, len(s1)

        if lg > len(s2):
            return False

        for i in range(lg):
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1

        for j in range(lg, len(s2)):
            if  arr1 == arr2:
                return True
            arr2[ord(s2[j-lg]) - ord('a')] -= 1
            arr2[ord(s2[j]) - ord('a')] += 1

        return arr1 == arr2










