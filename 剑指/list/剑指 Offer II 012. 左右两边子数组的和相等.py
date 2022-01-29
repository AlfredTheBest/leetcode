"""
https://leetcode-cn.com/problems/tvdfij/
https://leetcode-cn.com/problems/tvdfij/solution/python-qian-zhui-he-by-sdbu034-4aqi/
思路:
    遍历前缀和数组 若前缀和数组为pre_sum 对于下标i 其左侧所有元素相加的和为pre_sum[i], 其右侧所有元素相加的和
    为pre_sum[-1] - pre_sum[i+1] 判断二者是否相等

"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = 0
        pre_sum = [pre]

        for num in nums:
            pre += num
            pre_sum.append(pre)

        for index, pre in enumerate(pre_sum[:-1]):
            if pre == pre_sum[-1] - pre_sum[index + 1]:
                return index

        return -1