from pytest_unordered import unordered
from _01_arrays_and_hashing._05_top_k_frequent_elements import Solution

class TestSolution:
    def test_topKFrequent(self):
        assert Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2) == unordered([1,2])
        assert Solution().topKFrequent(nums = [1], k = 1) == unordered([1])
