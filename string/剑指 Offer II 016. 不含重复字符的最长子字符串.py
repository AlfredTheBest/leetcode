"""
https://leetcode-cn.com/problems/wtcaE1/
https://leetcode-cn.com/problems/wtcaE1/solution/shua-chuan-jian-zhi-offer-day09-zi-fu-ch-tb4t/
思路：
    哈希表+滑动窗口
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        calc = {}
        left = 0
        ret = 0
        for i, j in enumerate(s):
            if j in calc:
                left = max(left, calc[j] + 1)
            calc[j] = i
            ret = max(ret, i - left + 1)
        return ret