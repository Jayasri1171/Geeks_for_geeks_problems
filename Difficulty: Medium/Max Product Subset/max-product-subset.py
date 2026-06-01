class Solution:
    def findMaxProduct(self, arr):
        # code here
        pos=[]
        neg=[]
        zc=0
        modl=10**9+7
        for i in arr:
            if i>0:
                pos.append(i)
            elif i==0:
                zc+=1
            else:
                neg.append(i)
        ans=1
        for i in pos:
            ans=(ans*i)
            ans=ans%modl
        x=0
        neg.sort()
        if(len(neg)%2==0):
            while(x<len(neg)):
                ans=(ans*neg[x])
                ans=ans%modl
                x+=1
        else:
            while(x<len(neg)-1):
                ans=(ans*neg[x])
                ans=ans%modl
                x+=1
        if(arr==[0]):
            return 0
        if(len(arr)==1 and pos==[]):
            return arr[0]
        if(pos==[] and neg==[]):
            return 0
        if(len(neg)==1 and zc>0 and pos==[]):
            return 0
        # print(pos,neg,zc)
        return ans%modl