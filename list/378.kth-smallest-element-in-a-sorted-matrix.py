# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        start, end = matrix[0][0], matrix[-1][-1]

        while start < end:
            mid = (start + end) // 2
    

    def countMid(self, mid, matrix, k):

        n = len(matrix)
        row, col = n-1, 0
        count = 0

        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                col -= 1
        
        if count >= k:
            return True












































