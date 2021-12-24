"""
https://leetcode-cn.com/problems/1fGaJU/
剑指 Offer II 007. 数组中和为 0 的三个数
思路:
    三指针问题
    注意细节:
        剪枝： 升序 和为0 第一个指针肯定不能大于1
              num[i] == num[i-1]

"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            left = i + 1
            right = n - 1

            if nums[i] > 0:
                break

            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ret.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1

        return ret









