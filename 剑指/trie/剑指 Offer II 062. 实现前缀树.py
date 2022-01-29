"""
https://leetcode-cn.com/problems/QC3q1f/
思路:
    Trie
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        prefix = self.trie
        for i in range(len(word)):
            if word[i] not in prefix:
                prefix[word[i]] = {}
            prefix = prefix[word[i]]
        prefix['end'] = {}


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        prefix = self.trie
        for i in range(len(word)):
            if word[i] in prefix:
                prefix = prefix[word[i]]
            else:
                return False

        if 'end' in prefix:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.trie
        for i in range(len(prefix)):
            if prefix[i] in trie:
                trie = trie[prefix[i]]
            else:
                return False
        return True










