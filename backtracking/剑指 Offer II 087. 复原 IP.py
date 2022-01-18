"""
https://leetcode-cn.com/problems/0on3uN/
思路:
    backtrack
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(s, path):
            if len(s) == 0 and len(path) == 4:
                self.ans.append('.'.join(path))
                return

            if len(path) >= 4:
                return

            for i in range(min(3, len(s))):
                s1, s2 = s[:i+1], s[i+1:]
                if 0 <= int(s1) <= 255 and str(int(s1)) == s1:
                    path.append(s1)
                    backtrack(s2, path)
                    path.pop()

        self.ans = []
        backtrack(s, [])
        return self.ans








