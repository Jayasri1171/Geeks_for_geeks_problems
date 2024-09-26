//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    // Function to find maximum number of consecutive steps
    // to gain an increase in altitude with each step.
    int maxStep(vector<int>& arr) {
        // Your code here
        int maxx=0;
        int z=0;
        int initial=arr[0];
        for(int i=1;i<arr.size();i++){
            // cout<<z<<"\n";
            if (arr[i]>initial){
                initial=arr[i];
                z+=1;
            }
            else{
                if(z>maxx){
                    maxx=z;
                }
                z=0;
                initial=arr[i];
            }
            
        }
        if(z>maxx){
            maxx=z;
        }
        return maxx;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input); // Read the entire line for the array elements
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution ob;
        cout << ob.maxStep(arr) << endl;
    }
    return 0;
}
// } Driver Code Ends