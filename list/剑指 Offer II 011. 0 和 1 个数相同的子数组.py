"""
https://leetcode-cn.com/problems/A1NYOS/
https://leetcode-cn.com/problems/A1NYOS/solution/shua-chuan-jian-zhi-offer-day07-shu-zu-i-4q9c/
思路:
    前缀和
初始化哈希表 并添加{0:-1}
声明前缀和变量pre_sum = 0,最大子数组长度返回值ret = 0
循环数组 若元素为0 pre_sum - 1 反之pre_sum + 1
判断哈希表中是否存在值为pre_sum的key
若存在pre_sum的key,更新ret为max(ret, 当前下标 - key对应的value + 1)
return ret
"""

class Solution:
    def findMaxLength(self, nums):
        pre_dict = {0: -1}
        ret = pre_sum = 0

        for index, num in enumerate(nums):
            pre_sum += -1 if num == 0 else 1

            if pre_sum in pre_dict:
                ret = max(ret, index - pre_dict[pre_sum])
            else:
                pre_dict[pre_sum] = index

        return ret
