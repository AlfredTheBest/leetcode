"""
https://leetcode-cn.com/problems/lwyVBB/
https://leetcode-cn.com/problems/lwyVBB/solution/shua-chuan-jian-zhi-offer-day16-ha-xi-bi-mtik/
思路:
    根据order建立dict
    根据words order 比较words
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {j:i for i, j in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w1_len = words[i], len(words[i])
            w2, w2_len = words[i+1], len(words[i+1])
            for j in range(max(w1_len, w2_len)):
                w1_idx = -1 if j >= w1_len else dic[w1[j]]
                w2_idx = -1 if j >= w2_len else dic[w2[j]]

                if w1_idx > w2_idx:
                    return False
                if w1_idx < w2_idx:
                    break

        return True




























