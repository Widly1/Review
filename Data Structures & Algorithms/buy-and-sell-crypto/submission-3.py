class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # our variables to buy and sell and maxProfit
        min_price = float('inf')   # lowest price seen up to the current day
        max_profit = 0

        for price in prices:
            # potential profit if we sell today
            profit = price - min_price
            max_profit = max(max_profit, profit)

            # update the lowest purchase price seen so far
            min_price = min(min_price, price)

        return max_profit






