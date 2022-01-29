"""
https://leetcode-cn.com/problems/vEAB3K/
思路
    bfs
"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # BFS染色
        n = len(graph)
        colored = [-1 for i in range(n)]

        def bfs(i,color):# 参数为索引和颜色
            colored[i] = color
            queue = deque()
            queue.append(i) # 初始化
            while len(queue) != 0:
                e = queue.popleft()
                for neigh in graph[e]:
                    if colored[neigh] >= 0: # 如果已经被染色，检查
                        if colored[neigh] == colored[e]:
                            return False
                    elif colored[neigh] == -1: # 如果未被染色，染色成邻居的反色
                        queue.append(neigh)
                        colored[neigh] = 1 - colored[e]
            return True

        for i in range(n):
            if colored[i] == -1: # 开始染色
                if bfs(i,0) == False:
                    return False
        return True


