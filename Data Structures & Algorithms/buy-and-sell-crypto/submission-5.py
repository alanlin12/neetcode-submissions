class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr_cheapest = prices[0]
        for price in prices:
            curr_cheapest = min(curr_cheapest, price)
            res = max(res, price - curr_cheapest)
        
        return res