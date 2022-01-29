"""
https://leetcode-cn.com/problems/aseY1I/
给定一个字符串数组words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。
。
思路:
    暴力法 遍历所有单词对查看是否有相同的(利用set) 找不互相包含的最大的
"""

class Solution:
    def maxProduct(self, words):
        word_set = [set(word) for word in words]
        res = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if not word_set[i] & word_set[j]:
                    res = max(res, len(words[i]) * len(words[j]))

        return res