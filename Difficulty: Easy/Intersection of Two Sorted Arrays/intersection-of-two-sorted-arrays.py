class Solution:
    def intersection(self,a, b):
        c=set(a)
        ans=[]
        v=len(c)
        b=list(set(b))
        b.sort()
        for i in b:
            c.add(i)
            if(len(c)==v):
                ans.append(i)
            else:
                v+=1
        return ans
            