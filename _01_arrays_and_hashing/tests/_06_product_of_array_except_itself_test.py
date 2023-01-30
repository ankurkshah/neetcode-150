from _01_arrays_and_hashing._06_product_of_array_except_itself import Solution

class TestSolution:
    def test_productExceptSelf(self):
        assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]
        assert Solution().productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]