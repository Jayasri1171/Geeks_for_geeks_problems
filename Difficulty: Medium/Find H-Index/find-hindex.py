class Solution:
    def hIndex(self, citations):
        #code here
        citations.sort()
        ans=0
        i=0
        while(i<len(citations)):
            ans=max(ans,min(len(citations)-i,citations[i]))
            i+=1
        return ans