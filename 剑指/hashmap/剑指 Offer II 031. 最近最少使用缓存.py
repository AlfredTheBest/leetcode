"""
https://leetcode-cn.com/problems/OrIXps/
思路:
    使用orderddict
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()


    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key, False)
            self.cache.popitem(False)
        elif self.cap == len(self.cache):
            self.cache.popitem(False)
        self.cache[key] = value
