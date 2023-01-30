from pytest_unordered import unordered
from _01_arrays_and_hashing._04_group_anagrams import Solution

class TestSolution:
    def test_groupAnagrams(self):
        assert sorted(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])) == unordered([unordered(["bat"]),unordered(["ate","eat","tea"]),unordered(["nat","tan"])])
        assert sorted(Solution().groupAnagrams([""])) == [[""]]
        assert sorted(Solution().groupAnagrams(["a"])) == [["a"]]