"""
https://leetcode-cn.com/problems/sfvd7V/
https://leetcode-cn.com/problems/sfvd7V/solution/shua-chuan-jian-zhi-offer-day15-ha-xi-bi-p57n/

思路:
    map存位置 list存ret sorted(i)当作id
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        d = {}

        for i in strs:
            sort_i = ''.join(sorted(i))
            if sort_i in d:
                ret[d[sort_i]].append(i)
            else:
                d[sort_i] = len(ret)
                ret.append([i])
        return ret
