# https://leetcode.com/problems/3sum/description/
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-2):
            s = i+1
            e = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while s < e:
                thrsum = nums[i] + nums[s] + nums[e]
                if thrsum > 0:
                    e -= 1
                elif thrsum < 0:
                    s += 1
                else:
                    res.add((nums[i],nums[s],nums[e]))
                    s += 1
                    e -= 1
        return res 