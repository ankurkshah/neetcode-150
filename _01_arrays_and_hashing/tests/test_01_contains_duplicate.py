from _01_arrays_and_hashing._02_valid_anagram import Solution

class TestSolution:
    def test_isAnagram(self):
        assert Solution().isAnagram(s="anagram", t="nagaram")
        assert not Solution().isAnagram(s="cat", t="rat")