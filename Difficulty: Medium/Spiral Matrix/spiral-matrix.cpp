//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{

	public:
	int findK(vector<vector<int>> &a, int n, int m, int k)
    {
        vector<int>v;
        int top=0,bottom=n-1,left=0,right=m-1,dir=0;
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
        return v[k-1];
    }

};

//{ Driver Code Starts.

int main()
{
    int T;
    cin>>T;
  
    while(T--)
    {
        int n,m;
        int k=0;
        //cin>>k;
        cin>>n>>m>>k;
        vector<vector<int>> a(n, vector<int>(m, 0));
        
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cin>>a[i][j];
            }
        }

        Solution obj;

        cout<< obj.findK(a, n, m, k) << "\n";
        
       
    
cout << "~" << "\n";
}
}
// } Driver Code Ends