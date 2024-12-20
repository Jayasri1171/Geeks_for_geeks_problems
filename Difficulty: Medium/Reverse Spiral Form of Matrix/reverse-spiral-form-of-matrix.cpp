//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
    vector<int> reverseSpiral(int R, int C, vector<vector<int>>&a)  {
         vector<int>v;
        int top=0,bottom=R-1,left=0,right=C-1,dir=0;
        while(top<=bottom && left<=right){
            if(dir==0){
                for(int i=left;i<=right;i++){
                    v.push_back(a[top][i]);
                }
                top+=1;
            }
            else if(dir==1){
                for(int i=top;i<=bottom;i++){
                    v.push_back(a[i][right]);
                }
                right-=1;
            }
            else if(dir==2){
                for(int i=right;i>=left;i--){
                    v.push_back(a[bottom][i]);
                }
                bottom-=1;
            }
            else{
                for(int i=bottom;i>=top;i--){
                    v.push_back(a[i][left]);
                }
                left+=1;
            }
            dir=(dir+1)%4;
        }
        vector<int> temp(v.size());

    // Reverse copying the vector into temp vector
    reverse_copy(v.begin(), v.end(), temp.begin());

    // Copying back reversed vector
    v = temp;
        return v;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int R, C;
        cin>>R>>C;
        vector<vector<int>> a(R, vector<int>(C, 0));
        for(int i = 0;i < R*C;i++)
            cin>>a[i/C][i%C];
        Solution ob;
        vector<int>ans=ob.reverseSpiral(R,C,a);
        for(int i=0;i<ans.size();i++)cout<<ans[i]<<" ";
            cout<<endl;
    
cout << "~" << "\n";
}
    return 0;
}

// } Driver Code Ends