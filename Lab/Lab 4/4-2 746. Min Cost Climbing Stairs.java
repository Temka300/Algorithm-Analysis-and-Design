class Solution:
     def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(n):  
            if n < 2: 
                return cost[n] 
            return cost[n] + min(dp(n-1), dp(n-2))
		
        length = len(cost) 
        return min(dp(length-1), dp(length-2))