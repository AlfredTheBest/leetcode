"""
https://leetcode-cn.com/problems/group-anagrams/
思路:
    排序+hash
"""
import collections
class Solution:
    def groupAnagrams(self, strs):
        d = collections.defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            d[sorted_s].append(s)
        return list(d.values())





