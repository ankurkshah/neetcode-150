from _02_two_pointers._03_3_sum import Solution
from pytest_unordered import unordered

class TestSolution:
    def test_threeSum(self):
        assert Solution().threeSum(nums = [-1,0,1,2,-1,-4]) == [[-1,-1,2], [-1,0,1]]
        assert Solution().threeSum(nums = [0,1,1]) == []
        assert Solution().threeSum(nums = [0,0,0]) == [[0,0,0]]
        