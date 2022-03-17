"""
https://leetcode-cn.com/problems/XltzEq/
https://leetcode-cn.com/problems/XltzEq/solution/shua-chuan-jian-zhi-offer-day10-zi-fu-ch-y5ua/
思路：
    双指针
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum() and left < right:
                right -= 1
            else:
                if s[right].lower() != s[left].lower():
                    return False
                left += 1
                right -= 1
        return True







