from S_01_arrays_and_hashing.Q_01_contains_duplicate import Solution

class TestSolution:
    def test_containsDuplicate(self):
        assert Solution().containsDuplicate(nums = [1,2,3,1])
        assert not Solution().containsDuplicate(nums = [1,2,3,4])
        assert Solution().containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2])