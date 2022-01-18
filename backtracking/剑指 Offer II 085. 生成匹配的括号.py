"""
https://leetcode-cn.com/problems/IDBivT/
思路:
    backtrack
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backTrack(path, left, right):
            if left > n or right > n or right > left:
                return

            if left == n and right == n:
                ans.append(path)
                return
            backTrack(path + '(', left + 1, right)
            backTrack(path + ')', left, right + 1)

        backTrack('', 0, 0)
        return ans

