"""
https://leetcode-cn.com/problems/cuyjEf/
思路:
    bi-search

"""
import random


class Solution:
    def __init__(self, w):
        self.pre = list(accumulate(w))
        self.total = sum(w)

    def pickIndex(self):
        x = random.randint(1, self.total)
        return bisect_left(self.pre, x)





















