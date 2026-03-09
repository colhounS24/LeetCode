"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
"""

# Sliding Window; gets it done O(n)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1  # buy, sell
        max_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                # Profitable — calculate and update max
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # Found a cheaper price — shift buy pointer here
                left = right

            right += 1

        return max_profit