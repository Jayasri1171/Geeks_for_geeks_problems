#User function Template for python3

class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        l=[]
        if k==0:
            return 0
        summ=0
        d={0:1}
        ans=0
        for i in range(len(arr)):
            summ+=arr[i]
            if summ not in d:
                d[summ]=1
            else:
                d[summ]+=1
            if summ-k in d:
                ans+=d[summ-k]
                
        # print(d)
        return ans
            
                



