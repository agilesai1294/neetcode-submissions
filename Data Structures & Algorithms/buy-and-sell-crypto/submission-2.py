class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minPrice = float('inf')
        for price in prices:
            if price < minPrice:
                minPrice = price
            result = max(result, price-minPrice)
        return result