from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        buy_price = prices[0]

        for price in prices:

            buy_price = min(buy_price, price)

            profit = max(profit, price - buy_price)

        return profit
