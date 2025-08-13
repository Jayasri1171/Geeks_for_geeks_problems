class Solution:
    def minSoldiers(self, arr, k):
        # code here
        check=[]
        ans=0
        for i in arr:
            if(i%k==0):
                check.append(0)
                ans+=1
            else:
                check.append(k-(i%k))
        check.sort()
        if(len(arr)%2==0):
            req=len(arr)//2
        else:
            req=len(arr)//2+1
        # print(check)
        if(ans>=req):
            return 0
        else:
            z=check[0:req]
            return sum(z)
        