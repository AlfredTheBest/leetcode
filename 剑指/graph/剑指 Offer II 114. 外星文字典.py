"""
https://leetcode-cn.com/problems/Jf1JuT/
思路:
    建graph
"""

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 建 graph
        graph, inDegrees, isVaild = self.buildGraph(words)
        # 无效的情况
        if not isVaild:
            return ''
        # 拓扑排序
        order = self.getOrder(graph, inDegrees)
        # 获得结果
        if len(order) == len(graph):
            return ''.join(order)
        else:
            return ''

    def buildGraph(self, words):
        graph = dict()
        inDegrees = dict()
        isVaild = True
        # 先统计所有单词
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()
                if c not in inDegrees:
                    inDegrees[c] = 0
        # 建立 graph，一个是统计邻接表，一个是统计入度
        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]
            n1, n2 = len(word1), len(word2)
            # 针对 ['abc', 'ab'] 这种特殊情况，这是无效的输入，abc 不可能在 ab 前面
            # 学习 python startswith 的用法
            if word1 != word2 and word1.startswith(word2):
                isVaild = False
                break
            for j in range(min(n1, n2)):
                c1, c2 = word1[j], word2[j]
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        inDegrees[c2] += 1
                    break
        return graph, inDegrees, isVaild

    def getOrder(self, graph, inDegrees):
        queue = collections.deque()
        for c, degree in inDegrees.items():
            if degree == 0:
                queue.append(c)

        order = []
        while len(queue) > 0:
            c = queue.popleft()
            order.append(c)
            for next in graph[c]:
                inDegrees[next] -= 1
                if inDegrees[next] == 0:
                    queue.append(next)
        return order