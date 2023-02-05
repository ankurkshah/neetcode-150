from _03_sliding_windows._01_best_time_to_buy_and_sell_stock import Solution

class TestSolution:
    def test_maxProfit(self):
        assert Solution().maxProfit(prices = [7,1,5,3,6,4]) == 5
        assert Solution().maxProfit(prices = [7,6,5,3,1]) == 0