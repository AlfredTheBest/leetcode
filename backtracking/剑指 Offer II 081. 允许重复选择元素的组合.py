"""
https://leetcode-cn.com/problems/Ygoe9J/
思路:
    backtracking
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 回溯，无重复元素，根据剩余值凑成目标
        ans = []
        path = []
        candidates.sort() # 预先排序，
        # 收集逻辑为target == 0

        def backtracking(index,path,target):
            if index >= len(candidates) or target < 0:
                return
            if target == 0: # 收集条件
                ans.append(path[:])
                return
            for i in range(index,len(candidates)):  # 注意可以重复收集
                path.append(candidates[i])  # 做选择
                backtracking(i,path,target-candidates[i])
                path.pop() # 取消选择

        backtracking(0,[],target)
        return ans





