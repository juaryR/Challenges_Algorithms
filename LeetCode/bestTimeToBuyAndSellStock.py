## my solution but have a time Limit because have O(n²)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0 
#         maxProfit = 0 
#         for key, buy  in enumerate(prices):
#             for sell in range(key+1, len(prices)):
#                 if buy > prices[sell]:
#                     continue 
#                 profit =  prices[sell] - buy 
#                 maxProfit  = max(maxProfit,profit)
#         return maxProfit


# better solution from https://www.youtube.com/watch?v=UuiTKBwPgAo
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0 
        maxProfit = 0 
        l,r = 0,1
        while r < len(prices):
            if prices[l] < prices[r]:
                 profit = prices[r] - prices[l] 
                
                 maxProfit = max(maxProfit,profit)
            else:
                l = r 
            r +=1  
        return maxProfit 