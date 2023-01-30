from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        freq_map = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq_map[c].append(n)

        ans = []

        for i in range(len(freq_map)-1, 0, -1):
            for n in freq_map[i]:
                ans.append(n)
                if (len(ans) == k):
                    return ans