//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    // Function to find the smallest positive number missing from the array.
    int missingNumber(vector<int> &arr) {
        // Your code here
        sort(arr.begin(),arr.end());
        set<int> s(arr.begin(),arr.end());
        vector<int> ar(s.begin(),s.end());
        int j=0;
        for(int i=0;i<ar.size();i++){
            if(ar[i]>=1){
                j=i;
                break;
            }
        }
        int ch=1;
        
        for(int k=j;k<ar.size();k++){
            // cout<<ar[k]<<endl;
            if(ar[k]!=ch){
                return ch;
            }
            ch+=1;
        }
        return ch;
        
    }
};

//{ Driver Code Starts.

// int missingNumber(int arr[], int n);

int main() {

    // taking testcases
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {

        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        int result = ob.missingNumber(arr);
        cout << result << "\n";
    }
    return 0;
}
// } Driver Code Ends