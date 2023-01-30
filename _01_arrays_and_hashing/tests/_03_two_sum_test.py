from _01_arrays_and_hashing._03_two_sum import Solution

class TestSolution:
    def test_twoSum(self):
        assert sorted(Solution().twoSum(nums = [2,7,11,15], target = 9)) == [0,1]
        assert sorted(Solution().twoSum(nums = [3,2,4], target = 6)) == [1,2]
        assert sorted(Solution().twoSum(nums = [3,3], target = 6)) == [0,1]
 