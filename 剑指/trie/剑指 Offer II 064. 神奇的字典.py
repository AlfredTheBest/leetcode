"""
https://leetcode-cn.com/problems/US1pGT/
思路:
    Trie
"""

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def func(self, w1, w2):
        cnt = 0
        for i in range(0, len(w1)):
            if w1[i] != w2[i]:
                cnt += 1
            if cnt == 2:
                return False
        if cnt == 0:
            return False
        else:
            return True


    def buildDict(self, dictionary: List[str]) -> None:
        for i in range(0, len(dictionary)):
            if len(dictionary[i]) not in self.dict.keys():
                self.dict[len(dictionary[i])] = [dictionary[i]]
            else:
                self.dict[len(dictionary[i])].append(dictionary[i])

    def search(self, searchWord: str) -> bool:
        length = len(searchWord)
        if length not in self.dict.keys():
            return False
        else:
            for ele in self.dict[length]:
                if self.func(searchWord, ele):
                    return True
            return False






