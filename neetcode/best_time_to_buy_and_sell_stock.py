# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Solution: Sliding window
# The maximum profit is acquired when the lowest value is chosen before the highest value
# Use two pointers to iterate the list while finding the lowest value possible on the left and higest value possible on the right

def maxProfit(self, prices: List[int]) -> int:
    l, r = 0, 1
    ma_prof = 0
    
    while r < len(prices):
        if prices[l] < prices[r]:
            prof = prices[r] - prices[l]
            ma_prof = max(ma_prof, prof)
        else:
            l = r
    
        r += 1
        
    return ma_prof
