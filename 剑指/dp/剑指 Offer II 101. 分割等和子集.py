"""
https://leetcode-cn.com/problems/NUPfPr/
思路:
    dp

    dp[i][j]的含义是，选取前i个数，是否能凑到j
    状态转移方程: dp[i][j] 不选那个数，则dp[i][j] = dp[i-1][j]
    选取第i个数，dp[i][j] = dp[i-1][j-nums[i-1]]。第四个数的索引是3，第i个数的索引是i-1

"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        dp[j]表示 背包总容量是j，最大可以凑成j的子集总和为dp[j]。
        0-1 背包 1维实现
        倒序遍历是为了保证物品i只被放入一次！。但如果一旦正序遍历了，那么物品0就会被重复加入多次！
        """
        target = sum(nums)
        if target % 2 == 1: return False
        target //= 2
        dp = [0] * 10001
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        return target == dp[target]

class Solution:
    """
    01 背包 二维实现
    """
    def canPartition(self, nums: List[int]) -> bool:
        # 子集背包问题
        sumNum = sum(nums)
        if sumNum % 2 == 1:
            return False
        n = len(nums)
        sumNum //= 2
        # dp数组外加一圈
        # dp[i][j]的含义是，选取前i个数，是否能凑到j
        # 状态转移方程: dp[i][j] 不选那个数，则dp[i][j] = dp[i-1][j]
        # 选取第i个数，dp[i][j] = dp[i-1][j-nums[i-1]]。第四个数的索引是3，第i个数的索引是i-1
        dp = [[False for j in range(sumNum+1)] for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True

        for i in range(1,n+1):
            for j in range(1,sumNum+1):
                if j-nums[i-1] < 0: # 越界，塞不下，只能放弃塞
                    dp[i][j] = dp[i-1][j]
                elif j-nums[i-1] >= 0:
                    dp[i][j] = (dp[i-1][j] or dp[i-1][j-nums[i-1]]) # 有一个成立都是True
        return dp[-1][-1]



class Solution_v1:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:return False
        @cache
        def dp(i, j):
            if j < 0:return False
            if j == 0:return True
            if i == 0:return False
            return dp(i - 1,j - nums[i - 1]) or dp(i - 1,j)
        return dp(len(nums),s // 2)

