class Solution:
    def countDistinct(self, arr, k):
        # Code here
        d={}
        for i in range(k):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        ans=[]
        ans.append(len(d))
        i=1
        j=k
        while(j<len(arr)):
            if arr[j] not in d:
                d[arr[j]]=1
            else:
                d[arr[j]]+=1
            if(d[arr[i-1]]==1):
                del d[arr[i-1]]
            else:
                d[arr[i-1]]-=1
            ans.append(len(d))
            i+=1
            j+=1
        return ans
            
        
        