class Solution:
    def sumDiffPairs(self, arr, k):
        # code here
        arr.sort()
        i=len(arr)-1
        ans=0
        while(i>0):
            if(arr[i]-arr[i-1]<k):
                ans+=arr[i]+arr[i-1]
                i-=2
            else:
                i-=1
        return ans
            
            