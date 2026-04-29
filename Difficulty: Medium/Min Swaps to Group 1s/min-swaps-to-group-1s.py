class Solution:
    def minSwaps(self, arr):
        # code here
        onec=0
        for i in arr:
            if i==1:
                onec+=1
        if onec==0:
            return -1
        if onec==1:
            return 0
        i=0
        j=onec-1
        ans=len(arr)
        d=arr[0:onec]
        tmp=d.count(0)
        while(j<len(arr)):
            if(i!=0):
                if(arr[i-1]==0):
                    tmp-=1
                if(arr[j]==0):
                    tmp+=1
            ans=min(ans,tmp)
            i+=1
            j+=1
        return ans