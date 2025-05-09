//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int countBitsFlip(int a, int b) {
        // code here
        int count=0;
        while(a and b){
            if((a&1) != (b&1)){
                count+=1;
            }
            a=a>>1;
            b=b>>1;
        }
        if(a>0){
            while(a){
                if((a&1)==1){
                    count+=1;
                }
                a=a>>1;
            }
        }
        if(b>0){
            while(b){
                if((b&1)==1){
                    count+=1;
                }
                b=b>>1;
            }
        }
        return count;
    }
};


//{ Driver Code Starts.

// Driver Code
int main() {
    int t;
    cin >> t;   // input the testcases
    while (t--) // while testcases exist
    {
        int a, b;
        cin >> a >> b; // input a and b

        Solution ob;
        cout << ob.countBitsFlip(a, b) << endl;

        cout << "~"
             << "\n";
    }
    return 0;
}
// } Driver Code Ends