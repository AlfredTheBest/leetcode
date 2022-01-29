"""
https://leetcode-cn.com/problems/RQku0D/
https://leetcode-cn.com/problems/RQku0D/solution/shua-chuan-jian-zhi-offer-day10-zi-fu-ch-b0ub/
思路:
    首先设置左、右指针分别指向字符串的首尾
    然后开始左右匹配，如果相等left+1，right -1
    如果不相等，记录当前left和right，然后构造一个方法check
    想check中分别传输[left + 1,right]和[left, right - 1]，若检查通过返回True否则返回False
    如果3中有一个为True，就表示为回文子串。


"""
class Solution:
    def validPalindrome(self, s):
        def check(l, r):
            while l <= r:
                if s[l] != s[r]:
                    break
                l += 1
                r -= 1
            return l, r

        mid = len(s) // 2
        left, right = check(0, len(s) - 1)
        if left > mid:
            return True
        return check(left + 1, right)[0] > mid or check(left, right - 1)[0] >= mid
