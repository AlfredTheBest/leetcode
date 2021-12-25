"""
https://leetcode-cn.com/problems/VabMRr/

https://leetcode-cn.com/problems/VabMRr/solution/shua-chuan-jian-zhi-offer-day09-zi-fu-ch-f3mv/
双指针
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        arr1, arr2, lg, ret = [0] * 26, [0] * 26, len(p), []
        if lg > len(s):
            return []
        for i in range(lg):
            arr1[ord(p[i]) - ord('a')] += 1
            arr2[ord(s[i]) - ord('a')] += 1
        if arr1 == arr2:
            ret.append(0)
        for i in range(lg, len(s)):
            arr2[ord(s[i]) - ord('a')] += 1
            arr2[ord(s[i - lg]) - ord('a')] -= 1
            if arr1 == arr2:
                ret.append(i - lg + 1)
        return ret