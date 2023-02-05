from _02_two_pointers._04_container_with_most_water import Solution

class TestSolution:
    def test_maxArea(self):
        assert Solution().maxArea(height = [1,8,6,2,5,4,8,3,7]) == 49
        assert Solution().maxArea(height = [1,1]) == 1