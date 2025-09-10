class Solution:
    def largestSwap(self, s):
        #code here
        z=list(s)
        z.sort(reverse="True")
        ans=[]
        s=list(s)
        i=0
        while(i<len(s)):
            if s[i]!=z[i]:
                n=s[i]
                m=len(s) - 1 - s[::-1].index(z[i])
                s[i]=z[i]
                s[m]=n
                ans+=s[i]
                break
                
            else:
                ans+=s[i]
            i+=1
        # print(s)
        ans+=s[i+1::]
        # print(ans)
        ret=""
        for i in ans:
            ret+=i
            
        return ret
        
        