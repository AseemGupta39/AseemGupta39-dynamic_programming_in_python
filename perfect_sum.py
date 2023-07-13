class Solution:
    def perfectSum(self, arr, N, sum):
        ### iterative approach
        dp = [[0 for _ in range(sum+1)] for i in range(N)]
        mod = 10**9+7
        for j in range(sum+1):
            sm = j
            if sm==0:
                item = arr[0]
                if item ==0:
                    dp[0][j] =2
                else:
                    dp[0][j] = 1
            else:
                if item == sm:
                    dp[0][j]=1
                    
            
        
        for i in range(1,N):
            for j in range(sum+1):
                sm = j
                item  = arr[i]
                if item<=sm:
                    dp[i][j] =(dp[i-1][sm-item] + dp[i-1][sm])%mod
                else:
                    dp[i][j] = dp[i-1][sm]
                
        
        return dp[N-1][sum]
        
        ## recursive appraoch 
        
        # dp = {}
        # arr.sort(reverse=True)
        # mod = pow(10,9)+7
        # def solve(n,cap):
        #     if n==0: ## i item left 
        #         if cap == 0: ## if cap is zero  (0,1) wala case 
        #             return 1 
        #         return 0
        #     elif (n,cap) in dp:
        #         return dp[(n,cap)]
        #     else:
        #         item = arr[n-1]
        #         if item <= cap:
        #             c1 = solve(n-1,cap-item)
        #             c2 = solve(n-1,cap)
        #             c = (c1 + c2)%mod
        #         else:
        #             if cap==0: ## (2,1,0) wala case
        #                 c=1
        #             else:
        #                 c=0
        #     dp[(n,cap)] = c
        #     return c
        # return solve(N,sum)
                    
                


	       
        
        