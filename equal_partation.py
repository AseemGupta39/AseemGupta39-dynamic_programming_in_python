# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        #### iterative approach
        
        sm = sum(arr)
        
        if sm%2!=0:
            return False
            
        tar = sm//2
            
        dp = [[0 for _ in range(tar+1)] for i in range(N)]
        for i in range(N):
            for j in range(tar+1):
                item = arr[i]
                sm = j 
                if i==0:
                    if sm == 0 or item == sm:
                        dp[i][j] = 1
                else:
                    if item<=sm:
                        dp[i][j] = dp[i-1][sm-item] or dp[i-1][sm]
                    else: 
                        dp[i][j] = dp[i-1][sm]
        return  dp[N-1][tar]
        
        #### recursive approach
            
        # dp = {}
        # arr.sort(reverse=True)
        
        # def solve(n,cap):
        #     if n == 0:
        #         return False
        #     elif cap == 0:
        #         return True
        #     elif (n,cap) in dp:
        #         return dp[(n,cap)]
        #     else:
        #         current_item = arr[n-1]
        #         if current_item <= cap:
        #             choice_1 = solve(n-1,cap-current_item)
        #             choice_2 = solve(n-1,cap)
        #             c = choice_1 or choice_2
        #         else:
        #             c = 0
        #     dp[(n,cap)] = c
        #     return c
        
        # tar = sm//2
        
        # return solve(N,tar)