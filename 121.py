# 121. Best Time to Buy and Sell Stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
      
        diff1 = 0 #maximum difference
        min1 = prices[0] #minimum value

        for i in prices: #loop through array
            if i - min1 > diff1: #if the current index is a better sale replace
                diff1 = i - min1
            if i < min1: #if the current index is smaller than the min value replace
                min1 = i
              
        if diff1 < 0:
            diff1 = 0 #ignore negative values
        return diff1
