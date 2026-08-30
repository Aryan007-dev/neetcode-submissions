class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        p = 0 
        
        while r <len(prices):
            if prices[l]>prices[r]:
                l=r
                
            if prices[l]<prices[r]:
                np = prices[r]-prices[l]
                if np > p:
                    p = np
            r+=1
        return p              
