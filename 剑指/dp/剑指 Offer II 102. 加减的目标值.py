"""
https://leetcode-cn.com/problems/YaVDxD/
https://leetcode-cn.com/problems/YaVDxD/solution/jia-jian-de-mu-biao-zhi-by-leetcode-solu-be5t/
思路:
    dp
    dp[j] j 的容量最多能装多少

"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum = 0
        for num in nums:
            sum += num
        if (sum + target) % 2 == 1 or sum < target:
            return 0
        return self.subsetSum(nums, (sum + target) // 2)

    def subsetSum(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[target]



