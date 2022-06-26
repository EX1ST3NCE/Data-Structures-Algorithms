# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(prices):
        
        max_profit = 0
        minimum_so_far = prices[0]
        
        """
        We will store the minimum value in minimum_so_far, the minm value will get stored in it.
        E.g - [7,1,5,3,6,4] - First 7 will be the minimum value, then 1 will be the minm, and it will remain unchanged, 
                              as it is minimum value in the list. [7, 1, 1, 1, 1, 1]
                              
        Profit will have the differnce in prices of the selling and buying stocks. [0, 0, 4, 2, 5, 3]
        """
        
        for i in range(len(prices)):
            minimum_so_far = min(minimum_so_far, prices[i])
            profit = prices[i] - minimum_so_far
            max_profit = max(max_profit, profit)
            
        return max_profit
   
sol = Solution
print(sol.maxProfit([7,1,5,3,6,4]))     

"""
Time Complexity - 0(n)

Space Complexity - 0(n)
"""    