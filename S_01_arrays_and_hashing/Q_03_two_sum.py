from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prev_nums = {}

        for i,n in enumerate(nums):
            pair = target - n

            if pair in prev_nums:
                return [i, prev_nums[pair]]

            prev_nums[n] = i 