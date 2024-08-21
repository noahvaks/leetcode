# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #OH.. i was worried about revenue but it only asks about profit
        profit = 0 #current profit
        newMin = prices[0] #current minimum

        #ANY time there is a profit, I will make the purchase and then hold the current stock
        for i in prices:
            if i - newMin > 0: #if there is a profit
                profit += i - newMin #add profit and 'buy' current day.
                newMin = i
            if i < newMin: #'buy' new minimum
                newMin = i
        return profit
