# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/

"""
找第K个最小元素
就是当在两个值之间找第k个元素
二分法
"""

class Solution:
    def kthSmallest(self, matrix, k):

        n = len(matrix)

        def check(mid):
            i, j = n-1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += j + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]

        while left < right:
            mid = (left + right) // 2
            if check(mid): # mid >= k
                right = mid
            else:
                left = mid + 1

        return left




