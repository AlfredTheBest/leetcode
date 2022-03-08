"""
https://leetcode-cn.com/problems/wtcaE1/
https://leetcode-cn.com/problems/wtcaE1/solution/shua-chuan-jian-zhi-offer-day09-zi-fu-ch-tb4t/
思路：
    哈希表+滑动窗口

https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
模版
dict = {}
left = 0
ret = 0
for i, j in enumerate(s):
    业务处理

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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        rk , ans = 0, 0

        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])
            print(rk)
            while rk < n and  s[rk] not in occ:
                occ.add(s[rk])
                rk += 1
            ans = max(ans, rk - i)
        return ans