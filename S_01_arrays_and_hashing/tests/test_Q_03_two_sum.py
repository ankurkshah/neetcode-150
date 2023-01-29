from S_01_arrays_and_hashing.Q_03_two_sum import Solution

class TestSolution:
    def test_twoSum(self):
        assert Solution().twoSum(nums = [2,7,11,15], target = 9) in [ [0,1], [1,0] ]
        assert Solution().twoSum(nums = [3,2,4], target = 6) in [ [2,1], [1,2] ]
        assert Solution().twoSum(nums = [3,3], target = 6) in [ [0,1], [1,0] ]
        