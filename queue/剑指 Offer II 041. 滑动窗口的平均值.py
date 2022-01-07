"""
https://leetcode-cn.com/problems/qIsx9U/
https://leetcode-cn.com/problems/qIsx9U/solution/shua-chuan-jian-zhi-offer-day20-dui-lie-09ber/
思路:
    队列

"""


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.sum = 0
        self.size = size
        self.queue = deque()


    def next(self, val: int) -> float:
        self.sum += val
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.sum -= self.queue.popleft()
        return self.sum / len(self.queue)













