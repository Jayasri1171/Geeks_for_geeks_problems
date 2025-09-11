
class Solution {
  public:
    int minJumps(vector<int>& arr) {
        // code here
        int n=arr.size();
        if(n<=1){
            return 1;
        }
        if(arr[0]==0){
            return -1;
        }
        int steps=arr[0];
        int maxreach = arr[0];
        int jumps = 1;
        for(int i=1;i<n;i++){
            if(i==n-1) {
                return jumps;
            }
            
            maxreach = max(maxreach , i+arr[i]);
            steps--;
            if(steps == 0){
                jumps++;
                if(i>=maxreach){
                    return -1;
                }
                steps=maxreach-i;
            }
            // cout<<steps<<maxreach<<jumps<<endl;
        }
        return -1;
    }
};


