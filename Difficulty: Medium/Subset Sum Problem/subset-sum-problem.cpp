//{ Driver Code Starts

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    bool sums(vector<int>&a,int i,int s,int q)
  {
            if(q>s) return false;
            if (q==s) 
            {
            return true;
            }
            if (i==a.size())
            {
                return false;
            }
            if(sums(a,i+1,s,q+a[i]))
            {
               return true;
            }
            sums(a,i+1,s,q);
  }
    bool isSubsetSum(vector<int>& arr, int sum) {
         return sums(arr,0,sum,0);
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
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        int sum;
        cin >> sum;
        cin.ignore();

        Solution ob;
        if (ob.isSubsetSum(arr, sum))
            cout << "true" << endl;
        else
            cout << "false" << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends