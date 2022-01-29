"""
https://leetcode-cn.com/problems/ur2n8P/
https://leetcode-cn.com/problems/ur2n8P/solution/zhi-jie-jian-yan-by-ling-jian-2012-ftzj/

思路:
（前提）org中出现的数和seqs中出现的数的集合相同
（充分性）每个seq中相邻两个数在org中有相同的顺序
（必要性）org中相邻两个数一定是某个seq中的相邻的数
"""
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        edges = {(s[i], s[i+1])
                 for s in seqs
                 for i in range(len(s) - 1)}
        indices = [None] * len(org)
        for i, v in enumerate(org):
            indices[v - 1] = i
        return all((org[i], org[i+1]) in edges
                   for i in range(len(org) - 1)) and \
               {c for s in seqs for c in s} == set(org) and \
               all(indices[a-1] < indices[b-1] for a, b in edges)




