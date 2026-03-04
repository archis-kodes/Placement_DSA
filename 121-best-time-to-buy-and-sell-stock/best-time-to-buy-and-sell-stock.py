class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices [r]:
                #Profitable: Buy Low, Sell High
                profit = prices[r] - prices[l]  #calculate new profit
                maxP = max(maxP, profit)   #Store the maximum profit only
            else:
                #Found a R point much less than L point
                l=r  #Shift the left pointer straight to right one
            r+=1
        return maxP