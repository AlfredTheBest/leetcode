"""
https://leetcode-cn.com/problems/UhWRSj/
思路:
    Trie
"""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}

        for prefix in dictionary:
            root = trie
            for c in prefix:
                if c not in root:
                    root[c] = {}

                root = root[c]
            root[''] = ''

        words = sentence.split(' ')
        for i in range(len(words)):
            tmp, root = '', trie
            flag = False
            for c in words[i]:
                if c not in root:
                    break
                root = root[c]
                tmp += c
                if '' in root:
                    flag = True
                    break
            words[i] = tmp if flag else words[i]
        return ' '.join(words)













