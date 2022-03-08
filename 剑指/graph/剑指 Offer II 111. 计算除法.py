"""
https://leetcode-cn.com/problems/vlzXQL
思路:
    dfs
"""
import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic=collections.defaultdict(list)
        n=len(equations)
        for i in range(n):
            pair=equations[i]
            dic[pair[0]].append([pair[1],values[i]])
            dic[pair[1]].append([pair[0],1/values[i]])
        # 约分后即相当于找邻居,先转化成图
        # 已知不存在矛盾。【如果存在矛盾这一题需要收集所有可行路径然后比对所有路径值是否相等】
        def dfs(start,end,visited):
            if start not in dic or end not in dic: return -1.0
            if start==end: return 1.0
            visited.add(start)
            for x in dic[start]:
                nxt=x[0]
                if nxt not in visited:
                    val=dfs(nxt,end,visited)
                    if val>0:
                        return x[1]*val
            #visited.remove(start)
            return -1.0


        res=[]
        for q in queries:
            start=q[0]
            end=q[1]
            value=dfs(start,end,set())
            res.append(value)
        return res