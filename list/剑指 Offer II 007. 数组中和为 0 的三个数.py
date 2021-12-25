"""
https://blog.csdn.net/qq_36911138/article/details/104156073
https://leetcode-cn.com/problems/1fGaJU/
剑指 Offer II 007. 数组中和为 0 的三个数
思路:
    三指针问题
    注意细节:
        剪枝： 升序 和为0 第一个指针肯定不能大于1
              num[i] == num[i-1]

"""

class Solution:
    def threeSum_v1(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            left = i + 1
            right = n - 1

            if nums[i] > 0:
                break

            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ret.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1

        return ret

def bSearchV3(s, k):
    low = 0
    high = len(s) - 1
    while low <= high:
        mid = (low + high) // 2

        print(mid)


        if s[mid] <= k:
            low = mid + 1
        else:
            if mid == 0 or s[mid - 1] <= k:
                return mid
            else:
                high = mid - 1
    return -1

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def binary_search(s, k):
            # 在s中找比k大的第一个元素
            low = 0
            high = len(s) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if s[mid] <= k:
                    low = mid + 1
                else:
                    if mid == 0 or s[mid - 1] <= k:
                        return mid
                    else:
                        high = mid - 1


        res = []

        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1

        nums = sorted(dic)
        for i, x in enumerate(nums):
            if x == 0 and dic[x] > 2:
                res.append([0, 0, 0])
            elif x != 0 and dic[x] > 1:
                if -2 * x in dic:
                    res.append([x, x, -2 * x])

            if x < 0:
                y_z = -x
                z_id = binary_search(nums, y_z//2)

                if z_id:
                    for z in nums[z_id:]:
                        y = y_z - z

                        if y > x and y in dic:
                            res.append([x, y, z])

        return res






