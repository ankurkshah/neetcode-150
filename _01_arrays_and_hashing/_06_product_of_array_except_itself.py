from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        left_product, right_product = 1,1

        for i in range(len(nums)):
            ans[i] = left_product
            left_product = left_product * nums[i]

        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i] * right_product
            right_product = right_product * nums[i]

        return ans