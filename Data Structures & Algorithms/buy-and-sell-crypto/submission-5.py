class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')   # cheapest price up to now
        max_profit = 0             # best profit found so far

        for price in prices:
            # profit if we sell at the current price
            profit_today = price - min_price
            # keep the biggest profit seen
            max_profit = max(max_profit, profit_today)
            # maybe today is the new cheapest buying day
            min_price = min(min_price, price)

        return max_profit






