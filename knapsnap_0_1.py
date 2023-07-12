#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, N):
        #### ITERARIVE APPROACH II
        
        dp = [[0 for _ in range(W+1)] for _ in range(N)]
        
        
        cwt = wt[0]
        cv = val[0]
        for j in range(W+1):  ### SPECIAL CASE FOR i=0 MEANING 1 ITEM IS BEING LEFT
            cap = j
            if cwt<=cap:
                dp[0][j] = cv 
            else:
                dp[0][j] = 0
        
        for i in range(1,N):
            cwt = wt[i]
            cv = val[i]
            for j in range(W+1):
                cap = j
                if cwt<=cap:
                    c1 = cv + dp[i-1][cap-cwt]
                    c2 = 0+ dp[i-1][cap]
                    dp[i][j] = max(c1,c2)
                else:
                    dp[i][j] = dp[i-1][cap]
        return dp[N-1][W]
        
        
        #### iterative approach
        
        
        # dp = [[0 for _ in range(W+1)] for _ in range(N)]
        # for i in range(N):
        #     cwt = wt[i]
        #     cv = val[i]
        #     for j in range(W+1):
        #         cap = j
        #         if i == 0:
        #             if cwt<=cap:
        #                 dp[i][j] = cv 
        #             else:
        #                 dp[i][j] = 0
        #         else:
        #             if cwt<=cap:
        #                 c1 = cv + dp[i-1][cap-cwt]
        #                 c2 = 0+ dp[i-1][cap]
        #                 dp[i][j] = max(c1,c2)
        #             else:
        #                 dp[i][j] = dp[i-1][cap]
        # return dp[N-1][W]
                        
                
                
        
        
        
        
        #### recursive approach
        
        
        # dp = {}
        # def solve(n,cap):
        #     if n==0 or cap==0:
        #         return 0
        #     elif (n,cap) in dp:
        #         return dp[(n,cap)]
                
        #     else:
        #         cwt = wt[n-1]
        #         cv = val[n-1]
                
        #         if cwt<=cap:
        #             c1 = cv + solve(n-1,cap-cwt)
        #             c2 = solve(n-1,cap)
        #             c = max(c1,c2)
                    
        #         else:
        #             c = solve(n-1,cap)
        #     dp[(n,cap)] = c
        #     return c    
        # return solve(n,W)