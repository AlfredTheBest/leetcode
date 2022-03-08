"""
https://leetcode-cn.com/problems/WGki4K/

思路:
    依次确定每一个二进制位
    求数组中所有元素的第 i 个二进制位之和除以 3 的余数
"""

class Solution:
    def singleNumber(self, nums):
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        ans = [num for num, occ in freq.items() if occ == 1][0]
        return ans









