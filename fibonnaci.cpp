#include <iostream>
#include <vector>
using namespace std;

long long int fib(int n,vector<long long int> &dp){
    if (n==0 || n==1){
        return n;
    }
    else if(dp[n]!=-1){
        return dp[n];
    }
    else{
        dp[n] = fib(n-2,dp)+fib(n-1,dp);
        return dp[n];
    }
    
}


int main(){
    cout << "enter n: ";
    int n,i;
    cin >> n;

    vector<long long int> dp(n+1);
    
    // for(i=0;i<=n;i++){
    //     dp[i]=-1;
    // }
    
    // cout << "ans is: " << fib(n,dp) << "\n";

    dp[0] = 0;
    dp[1] = 1;
    for(i=2;i<n+1;i++){
        dp[i] = dp[i-1]+dp[i-2];
    }

    cout<<dp[n];

    return 0;
}