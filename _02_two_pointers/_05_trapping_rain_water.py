from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        ans = 0

        l, r = 0, len(height)-1

        l_wall, r_wall = height[l], height[r],

        while l < r:

            if l_wall < r_wall:
                l += 1
                l_wall = max(l_wall, height[l])
                ans += l_wall - height[l]
            else:
                r -= 1
                r_wall = max(r_wall, height[r])
                ans += r_wall - height[r]

        return ans
