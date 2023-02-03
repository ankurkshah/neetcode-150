from _02_two_pointers._02_two_sum_ii import Solution

class TestSolution:
    def test_twoSum(self):
        assert Solution().twoSum(numbers=[2,7,11,15], target=9) == [1,2]
        assert Solution().twoSum(numbers=[2,3,4], target=6) == [1,3]
        assert Solution().twoSum(numbers=[-1,0], target=-1) == [1,2]
