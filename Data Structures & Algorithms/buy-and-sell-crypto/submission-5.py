class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxdiff = 0

        while r < len(prices):
            diff = prices[r] - prices[l]
            maxdiff = max(maxdiff, diff)

            if diff < 0:
                l  = r 
            
            r += 1
        return maxdiff            
            