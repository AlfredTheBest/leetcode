"""
https://leetcode-cn.com/problems/2bCMpM/
思路
    bfs
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        distance=[[0]*n for _ in range(m)]
        que=collections.deque([(i,j) for i in range(m) for j in range(n) if mat[i][j]==0])
        while que:
            i,j=que.popleft()
            for x,y in [(i,j-1),(i,j+1),(i-1,j),(i+1,j)]:
                if 0<=x<m and 0<=y<n and mat[x][y]==1:
                    distance[x][y]=distance[i][j]+1
                    mat[x][y]=0
                    que.append((x,y))
                    #因为我们是从零周围开始循环的，而且还是一圈一圈地往外（广度优先）循环，
                    #所以之前计算过的点的distance一定<=现在的点的distance，所以不用再计算了。
                    #把它置0，防止下次循环到。
        return distance

