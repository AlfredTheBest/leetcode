"""
https://leetcode-cn.com/problems/M1oyTv/submissions/
https://leetcode-cn.com/problems/M1oyTv/solution/cpython3java-hua-dong-chuang-kou-lin-jie-5cb0/
思路:
    滑动窗口+临界统计
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for c in t:
            need[c] += 1

        needCnt = len(t)
        left = 0
        res = (0, len(s) + 1)
        for index, value in enumerate(s):
            if need[value] > 0:
                needCnt -= 1
            need[value] -= 1

            if needCnt == 0:
                while True:
                    left_value = s[left]
                    if need[left_value] == 0:
                        break
                    need[left_value] += 1
                    left += 1
                if index - left < res[1] - res[0]:
                    res = (left, index)
                needCnt += 1
                need[s[left]] += 1
                left += 1

        return '' if res[1] > len(s) else s[res[0]:res[1]+1]

