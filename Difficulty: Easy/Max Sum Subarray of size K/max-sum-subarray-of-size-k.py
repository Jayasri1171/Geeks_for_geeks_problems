class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        i=0
        j=k-1
        ans=sum(arr[i:j+1])
        i+=1
        j+=1
        fans=ans
        while(j<len(arr)):
            # print(arr[i],arr[j])
            ans+=arr[j]
            ans-=arr[i-1]
            i+=1
            j+=1
            if(ans>fans):
                fans=ans
        return fans