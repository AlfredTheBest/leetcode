"""
https://leetcode-cn.com/problems/FortPu/
思路:
    使用 dict和list实现
"""

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = {}
        self.l = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.s.keys():
            return False
        self.s[val] = len(self.l)
        self.l.append(val)
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.s.keys():
            self.s[self.l[-1]] = self.s[val]
            self.l[self.s[val]] = self.l[-1]
            self.l.pop()
            del self.s[val]
            return True
        return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.l)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()