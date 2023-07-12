class Solution:
    def isSubsetSum (self, N, arr, sum):
        ### iterative appraoch
        
        dp = [[0 for _ in range(sum+1)] for i in range(N)]
        for i in range(N):
            for j in range(sum+1):
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
        return  dp[N-1][sum]


        ### recursive approach
        
        # dp={}
        # arr.sort(reverse = True)
        # def solve(n,cap):
        #     if cap == 0:
        #         return True
        #     elif n == 0:
        #         return False
        #     elif (n,cap) in dp:
        #         return dp[(n,cap)]
        #     else:
        #         current_item = arr[n-1]
        #         if current_item<=cap:
        #             choice_1 = solve(n-1,cap-current_item)
        #             choice_2 = solve(n-1,cap)
        #             c = choice_1 or choice_2
        #         else: 
        #             choice_3 = 0 ## current item is bigger than sum
        #             c = choice_3
        #         dp[(n,cap)] = c
        #         return c
        # return solve(N,sum)


s = Solution()
N=6
arr =[3, 34, 4 ,12, 5, 2]
sum=9
print(s.isSubsetSum(N,arr,sum))