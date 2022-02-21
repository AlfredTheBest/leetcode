"""
https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
思路:
    backtrack
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        s = ''
        letterMap = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        if not len(digits): return res
        n  = len(digits)

        def backtrack(digits, index, s):
            if index == n:
                res.append(s)
                return
            digit = int(digits[index])

            letters = letterMap[digit]
            for letter in letters:
                s += letter
                backtrack(digits, index + 1, s)
                s = s[:-1]
        backtrack(digits, 0, s)

        return res










