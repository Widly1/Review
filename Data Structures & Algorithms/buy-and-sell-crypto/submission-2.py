class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        so we are given an array that isn't sorted and it doesn't have to be
        we have to choose a low day to buy a stock(lowest price if possible), and a day after that day to sell high (the max price we see after that day)
        so i.e: we buy at 1 sell at 5, max profit is 4
                    we buy at 1 sell at 6, max profit is 5
                    we buy at 1 sell at 7, max profit is 6
            so if we initialize 2 pointers, our l pointer would be where we buy
            and our r pointer would be where we sell
            we can iterate through the arr check our if l pointer is greater than r
        """          

        l = 0
        r = 0
        maxP = float('-inf')
        low = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r 
            made = prices[r] - prices[l]
            maxP = max(maxP, made)

            r += 1
        return maxP


