class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxp = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            maxp = max(maxp, profit)
            if prices[l] <= prices[r]:
                r += 1
            else:
                l = r
        
        return maxp

