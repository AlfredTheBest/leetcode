"""
https://leetcode-cn.com/problems/XagZNi/
https://leetcode-cn.com/problems/XagZNi/solution/shua-chuan-jian-zhi-offer-day17-zhan-i-0-5yho/
思路:
    分析场景 什么时候可以入什么时候需要pop 什么时候需要过掉

"""





class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s, p = [], 0
        while p < len(asteroids):
            if not s or s[-1] < 0 or asteroids[p] > 0:
                s.append(asteroids[p])
            elif s[-1] <= -asteroids[p]:
                if s.pop() < -asteroids[p]:
                    continue
            p += 1
        return s



