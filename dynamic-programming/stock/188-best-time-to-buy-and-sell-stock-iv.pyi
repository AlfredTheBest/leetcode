# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/submissions/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        length = len(prices)
        if len(prices) == 0 or k == 0:
            return 0

        dp = [[0] * 2 * k for _ in range(length)]
        for j in range(0, 2* k, 2):
            dp[0][j] = -prices[0]
        for i in range(1, length):
            for j in range(0, 2 * k, 2):
                if j == 0:
                    dp[i][j] = max(dp[i - 1][j], -prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] + prices[i])

        return dp[-1][2 * k - 1]

















































