# https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/

import heapq


class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = []
        n = len(nums)

        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        for i in range(k, n):
            heapq.heappush(q, -(-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans
