from _02_two_pointers._01_valid_palindrome import Solution

class TestSolution:
    def test_isPalindrome(self):

        assert Solution().isPalindrome(s = "A man, a plan, a canal: Panama")
        assert not Solution().isPalindrome(s = "race a car")
        assert Solution().isPalindrome(s= " ")
        assert Solution().isPalindrome(s = ".,")