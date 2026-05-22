class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cheapest price up to now
        minPrice= float('inf')
        # best profit found so far
        biggest = 0

        # iterate though the prices 
        for price in prices:
            # profit if we sell at the current price
            profit = price - minPrice
            
            # keep the biggest profit seen thus far between biggest and current profit
            biggest = max(biggest, profit)
            
            # maybe today is the new cheapest buying day(check the min price to make sure we bought at the lowest)
            minPrice = min(minPrice, price)
          
        # return max profit
        return biggest






