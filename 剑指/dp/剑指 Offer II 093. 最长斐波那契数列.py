"""
https://leetcode-cn.com/problems/Q91FMA/

思路:
    dp
        dp[i][j] 表示以 arr[i], arr[j] 为结尾的 j 状态下的最长斐波那契序列长度

        dp[i][j] = max(dp[j-i][i] + 1, dp[i][j])

        ans = 0
        return max(dp)
"""
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        record = {}
        # dp[i][j] 表示以 arr[i], arr[j] 为结尾的 j 状态下的最长斐波那契序列长度
        dp = [[2]*n for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                before = arr[j] - arr[i]
                if before in record:
                    dp[i][j] = max(dp[i][j], dp[record[before]][i] + 1)
                    ans = max(ans, dp[i][j])

            record[arr[i]] = i

        return ans if ans > 2 else 0









