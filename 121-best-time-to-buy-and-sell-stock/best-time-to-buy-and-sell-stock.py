class Solution(object):
    def maxProfit(self, prices):

        #If there's only one day or less in the market, there's no possible profit
        maxProfit = 0
        if len(prices) <= 1 : return maxProfit 

        buy , sell = 0, 1
        while sell < len(prices):
            if prices[sell] > prices[buy]:
            #if there's a positive slow, then it's worth checking if this is a new maxProfit
                maxProfit = prices[sell]-prices[buy] if prices[sell]-prices[buy] > maxProfit else maxProfit
                sell+=1
            #If there's a negative slope just hold the stock for another day
            elif prices[sell] < prices[sell-1] and prices[sell] > prices[buy]:
                sell+=1
            #If encountered a cheaper day than what we currently had, buy that one 
            elif prices[sell] < prices[sell-1] and prices[sell] < prices[buy]:
                buy = sell
                sell += 1 
            else: sell += 1
        #Buy low, sell high
        return maxProfit