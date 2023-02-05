from _03_sliding_windows._02_longest_substring_without_repeating_characters import Solution

class TestSolution:
    def test_lengthOfLongestSubstring(self):
        assert Solution().lengthOfLongestSubstring(s = "abcabcbb") == 3
        assert Solution().lengthOfLongestSubstring(s = "bbbbbb") == 1
        assert Solution().lengthOfLongestSubstring(s = "pwwkew") == 3
