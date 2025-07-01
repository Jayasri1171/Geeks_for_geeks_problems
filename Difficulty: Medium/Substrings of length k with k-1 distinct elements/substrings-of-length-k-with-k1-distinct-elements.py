class Solution:
    def substrCount(self, s, k):
        # code here
        ans=0
        i=0
        j=k
        while(j<=len(s)):
            m=s[i:j]
            l=list(set(m))
            if(len(l)==k-1):
                ans+=1
            i+=1
            j+=1
        return ans
        