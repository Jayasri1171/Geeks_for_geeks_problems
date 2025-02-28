//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int evaluate(vector<string>& arr) {
        // code here
        stack<int>s;
        for(string i : arr){
            if (i=="+" or i=="-" or i=="*" or i=="/"){
                int b=s.top();
                s.pop();
                int a=s.top();
                s.pop();
                if(i=="+") s.push(a+b);
                if(i=="-") s.push(a-b);
                if(i=="*") s.push(a*b);
                if (i=="/") s.push(a/b);
            }
            else{
                s.push(stoi(i));
            }
        }
        return s.top();
    }
};


//{ Driver Code Starts.

int main() {
    string str;
    getline(cin, str);
    int t = stoi(str);
    while (t--) {
        getline(cin, str);
        stringstream ss(str);
        vector<string> arr;
        while (ss >> str) {
            arr.push_back(str);
        }
        Solution ob;
        cout << ob.evaluate(arr) << endl;
        cout << "~" << endl;
    }
}
// } Driver Code Ends