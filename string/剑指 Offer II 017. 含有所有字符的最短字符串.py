"""
https://leetcode-cn.com/problems/M1oyTv/submissions/
https://leetcode-cn.com/problems/M1oyTv/solution/cpython3java-hua-dong-chuang-kou-lin-jie-5cb0/
思路:
    滑动窗口+临界统计
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n: return ""
        hashmap = Counter(t)
        count = len(t)
        i, j = 0,0

        tmpLen = m + 1
        ans = ''
        while j < m:
            if s[j] in hashmap:
                if hashmap[s[j]] > 0:
                    count -= 1
                hashmap[s[j]] -= 1

            while count == 0:
                if tmpLen > j - i + 1:
                    tmpLen = j - i + 1
                    ans = s[i:j+1]

                if s[i] in hashmap:
                    if hashmap[s[i]] >= 0:
                        count += 1
                    hashmap[s[i]] += 1
                i += 1
            j += 1
        return ans

