from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        areaMax = 0
        while left < right:
            areaMax = max(min(height[left], height[right])
                          * (right - left), areaMax)

            if height[left] < height[right]:
                left = left + 1

            else:
                right = right - 1
        return areaMax
