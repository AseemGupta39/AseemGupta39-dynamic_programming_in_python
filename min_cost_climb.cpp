#include <iostream>
#include <vector>
using namespace std;

#define MOD 1000000007;

// int solve(long long nStairs,int i){
//     if(i==nStairs){
//         return 1;
//     }
//     if(i>nStairs){
//         return 0;
//     }
//     return (solve(nStairs,i+1)+solve(nStairs,i+2))%MOD;
// }

int countWays(long long nStairs){
    // int ans = solve(nStairs,0);
    // vector<long long> dp(nStairs+1);
    long long dp[nStairs+1];
    dp[0] = 1;
    dp[1] = 1;
    int i;
    for(i=2;i<nStairs+1;i++){
        dp[i] = (dp[i-1]+dp[i-2])%MOD;
    }
    
    return dp[nStairs];
}

int main(){
    int n;
    cin >> n;
    cout << countWays(n);
    return 0;
}