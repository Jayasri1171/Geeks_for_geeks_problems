class Solution:
    def findMean(self, arr, queries):
        # code here
        prfsum=[]
        tmp=0
        for i in arr:
            tmp+=i
            prfsum.append(tmp)
        ans=[]
        # print(prfsum)
        for i in queries:
            if(i[0]!=0):
                op=prfsum[i[1]]-prfsum[i[0]-1]
            else:
                op=prfsum[i[1]]
            z=i[1]-i[0]+1
            ans.append(op//z)
        return ans