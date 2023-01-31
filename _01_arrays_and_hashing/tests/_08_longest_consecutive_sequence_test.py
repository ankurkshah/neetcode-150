from _01_arrays_and_hashing._08_longest_consecutive_sequence import Solution

class TestSolution:
    def test_longestConsecutive(self):

        assert Solution().longestConsecutive(nums=[100,4,200,1,3,2]) == 4
        assert Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]) == 9