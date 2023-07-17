#include <bits/stdc++.h> 
using namespace std;
int minimumElements(vector<int> &v, int x)
{
    // Write your code here.
    if(x==0){
        return 0;
    }
    int count = 0;
    sort(v.begin(),v.end());
    reverse(v.begin(),v.end());
    for(int i:v){
        while(x>=i){
            x-=i;
            count++;
        }
    }
    if(x!=0){
        return -1;
    }

    return count;
}

int main(){

    int t,n,x,i;
    cin >> t;
    while(t--){
        cin >> n >> x;
        vector<int> v(n);
        for(i=0;i<n;i++){
            cin >> v[i];
        }
        cout << "count is: " << minimumElements(v,x) << "\n";
    }
}

/*
2
3 7
1 2 3
1 0
1
*/