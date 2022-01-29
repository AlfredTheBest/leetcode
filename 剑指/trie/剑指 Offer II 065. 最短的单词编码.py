"""
https://leetcode-cn.com/problems/iSwD2y/
思路:
    1. Trie
    2. 去后缀
"""

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # 去重
        good = set(words)
        for word in words:  # 索引每个字符串
            # 如果good中有这些字符串的后缀，就直接去除，因为已经包含，是不用考虑的
            for k in range(1,len(word)):
                good.discard(word[k:])
        return sum(len(word)+1 for word in good)
