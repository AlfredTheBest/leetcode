"""
https://leetcode-cn.com/problems/QTMn0o/

https://leetcode-cn.com/problems/QTMn0o/solution/shua-chuan-jian-zhi-offer-day07-shu-zu-i-jdnu/
思路：前缀和
初始化一个空的哈希表和pre_sum=0的前缀和变量
设置返回值ret = 0，用于记录满足题意的子数组数量
循环数组的过程中，通过原地修改数组的方式，计算数组的累加和
将当前累加和减去整数K的结果，在哈希表中查找是否存在
如果存在该key值，证明以数组某一点为起点到当前位置满足题意，ret加等于将该key值对应的value
判断当前的累加和是否在哈希表中，若存在value+1，若不存在value=1
最终返回ret即可

"""
class Solution:
    def subarraySum(self, nums, k):
        pre_sum = ret = 0
        pre_dict = {0: 1}

        for i in nums:
            pre_sum += i
            ret += pre_dict.get(pre_sum - k, 0)
            pre_dict[pre_sum] = pre_dict.get(pre_sum, 0) + 1

        return ret

















