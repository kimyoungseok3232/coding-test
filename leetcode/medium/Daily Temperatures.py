# https://leetcode.com/problems/daily-temperatures/description/
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]
        
        for idx, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                s = stack.pop()
                res[s] = idx - s
            stack.append(idx)
        return res