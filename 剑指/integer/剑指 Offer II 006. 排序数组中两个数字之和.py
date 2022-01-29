"""
https://leetcode-cn.com/submissions/detail/251212237/
思路:
    常规双指针问题
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left, right]
            elif sum > target:
                right -= 1
            else:
                left += 1

        return []
















