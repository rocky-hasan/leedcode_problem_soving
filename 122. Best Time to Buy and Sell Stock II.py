class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy=prices[0]
        n=len(prices)
        profit=0
        for sell in prices:
            if buy<sell:             
                profit +=sell-buy
                print(f'profit: {profit}')  
            buy=sell 
            print(f'buy: {buy}')
           
        return profit
prices =[7,1,5,3,6,4]
res=Solution()
ans=res.maxProfit(prices)
print(f'ans: {ans}')