"""
https://leetcode-cn.com/problems/H8086Q/
https://leetcode-cn.com/problems/H8086Q/solution/shua-chuan-jian-zhi-offer-day18-zhan-ii-de51o/
思路:
    队列
"""
class RecentCounter:

    def __init__(self):
        self.req = deque()


    def ping(self, t: int) -> int:
        self.req.append(t)
        while self.req[0] < t - 3000:
            self.req.popleft()

        return len(self.req)



