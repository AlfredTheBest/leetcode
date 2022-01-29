"""
https://leetcode-cn.com/problems/fi9suh/

思路:


"""


class MyCalendar:

    def __init__(self):
        self.start = []
        self.end = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_right(self.end, start)
        if idx == len(self.end) or end <= self.start[idx]:
            bisect.insort(self.start, start)
            bisect.insort(self.end, end)
            return True
        return False


class MyCalendar:

    def __init__(self):
        self.time = []


    def book(self, start: int, end: int) -> bool:
        for s,e in self.time:
            if end>s and e>start:
                return False
        self.time.append([start,end])
        return True





