'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day 
in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit,
 return 0.'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0 
        right = 1 
        max_profit = 0  
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit
        

   
prices = [7,1,5,3,6,4] 
res=Solution()
ans=res.maxProfit(prices)
print(ans)



