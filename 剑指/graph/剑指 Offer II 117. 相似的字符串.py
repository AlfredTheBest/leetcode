"""
https://leetcode-cn.com/problems/H6lPxb
思路:
    dfs
"""
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        def check(wordx: str, wordy: str) -> bool:
            wn = len(wordx)
            cnt = 0
            for i in range(wn):
                if wordx[i] != wordy[i]:
                    cnt += 1
                    if cnt > 2:
                        return False
            return cnt == 0 or cnt == 2


        def dfs(sx):
            for y in range(n):
                if visited[y] == False and check(strs[sx], strs[y]) == True:
                    visited[y] = True
                    dfs(y)

        n = len(strs)
        visited = [False for _ in range(n)]
        cnt = 0

        for x in range(n):
            if visited[x] == False:
                visited[x] = True
                dfs(x)
                cnt += 1

        return cnt




