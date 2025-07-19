class Solution:
    def vowelCount(self, s):
        #code here
        cou=0
        check=['a','e','i','o','u']
        l={}
        def fact(n):
            if n<=1:
                return 1
            else:
                return n*fact(n-1)
        
        for i in s:
            if i in check:
                cou+=1
                if i not in l:
                    l[i]=1
                else:
                    l[i]+=1
        ans=fact(len(l))
        for i in l:
            ans=ans*l[i]
        if cou==0:
            return 0
        return ans