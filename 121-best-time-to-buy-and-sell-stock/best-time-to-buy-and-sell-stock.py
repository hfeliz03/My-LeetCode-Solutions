class Solution(object):
    def maxProfit(self, prices):

        #If only one day or less in the market, there's no possible profit
        maxProfit = 0
        if len(prices) <= 1 : return maxProfit 

        buy , sell = 0, 1
        while sell < len(prices):
            if prices[sell] > prices[buy]:
            #if positive slope, it's worth checking if this is a new maxProfit
                maxProfit = prices[sell]-prices[buy] if prices[sell]-prices[buy] > maxProfit else maxProfit
                sell+=1

            #If negative slope, hold the stock for another day
            elif prices[sell] < prices[sell-1] and prices[sell] > prices[buy]:
                sell+=1

            #If encountered a cheaper day than what we currently had, buy that one 
            elif prices[sell] < prices[sell-1] and prices[sell] < prices[buy]:
                buy = sell
                sell += 1 

            #If buy and low are the same price, hold stock one more day    
            else: sell += 1

        #Buy low, sell high
        return maxProfit