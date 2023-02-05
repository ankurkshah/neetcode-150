from _02_two_pointers._05_trapping_rain_water import Solution

class TestSolution:
    def test_trap(self):
        assert Solution().trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]) == 6
        assert Solution().trap(height = [4,2,0,3,2,5]) == 9
        assert Solution().trap(height = [5,4,1,2]) == 1
