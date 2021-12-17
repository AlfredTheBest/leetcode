
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [[0] * 2 for _ in range(length)]

        if length == 0:
            return 0
        dp[0][0] = -prices[0]

        for i in range(1, length):
            dp[i][0] = max(dp[ i -1][0], -prices[i])
            dp[i][1] = max(dp[ i -1][1], dp[ i -1][0] + prices[i])

        return dp[-1][1]


class Solution_v1:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [[0] * 2 for _ in range(2)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i % 2][0] = max(dp[(i - 1) % 2][0], -prices[i])
            dp[i % 2][1] = max(dp[(i - 1) % 2][1], prices[i] + dp[(i - 1) % 2][0])

        return dp[(length - 1) % 2][1]

























