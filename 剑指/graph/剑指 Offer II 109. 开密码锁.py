"""
https://leetcode-cn.com/problems/zlDJc7/
思路:
    bfs
"""
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if target == '0000':
            return 0

        dead = set(deadends)
        if "0000" in dead:
            return -1

        def num_prev(x):
            return '9' if x == '0' else str(int(x) - 1)

        def num_succ(x):
            return '0' if x == '9' else str(int(x) + 1)

        def get(status):
            s = list(status)

            for i in range(4):
                num = s[i]
                s[i] = num_prev(num)
                yield "".join(s)
                s[i] = num_succ(num)
                yield "".join(s)
                s[i] = num

        q = deque([('0000', 0)])
        seen = {'0000'}
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                if next_status not in seen and next_status not in dead:
                    if next_status == target:
                        return step + 1
                    q.append((next_status, step + 1))
                    seen.add(next_status)
        return -1

