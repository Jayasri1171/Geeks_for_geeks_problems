class Solution:
    def minToggle(self, arr):
        # code here
        no_of_ones=[]
        chk=0
        onec=arr.count(1)
        zeroc=arr.count(0)
        if(onec==0 or zeroc==0):
            return 0
        for i in arr:
            if i==1:
                chk+=1
            no_of_ones.append(chk)
        # print(no_of_ones)
        no_of_zeros=[]
        chk=0
        for i in range(len(arr)-1,-1,-1):
            no_of_zeros.append(chk)
            if arr[i]==0:
                chk+=1
        no_of_zeros=no_of_zeros[::-1]
        ans=2345678989999876
        for i in range(len(arr)):
            tmp=no_of_ones[i]+no_of_zeros[i]
            ans=min(ans,tmp)
        ans=min(ans,onec)
        ans=min(ans,zeroc)
        return ans
            