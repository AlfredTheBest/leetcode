"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1 // 初始化
        length = len(nums)

        while left <= right: // loop
            mid = (left + right) // 2 # mid 逻辑

            # 处理逻辑
            if nums[mid] == target:
                n = m = mid
                while n > 0 and nums[n] == nums[n-1]:
                    n -= 1

                while m < length - 1 and nums[m] == nums[m + 1]:
                    m += 1

                return [n, m]

            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return [-1, -1]

"""