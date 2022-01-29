"""
https://leetcode-cn.com/problems/QA2IGt/
思路:
    bfs
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        N = numCourses

        adjvex = defaultdict(list)
        indegree = [0 for _ in range(N)]
        for y, x in prerequisites:
            adjvex[x].append(y)
            indegree[y] += 1


        q = deque()
        for x in range(N):
            if indegree[x] == 0:
                q.append(x)

        res = []
        cnt = 0
        while q:
            x = q.popleft()
            res.append(x)
            cnt += 1
            for y in adjvex[x]:
                indegree[y] -= 1
                if indegree[y] == 0:
                    q.append(y)
        return res if cnt == N else []

