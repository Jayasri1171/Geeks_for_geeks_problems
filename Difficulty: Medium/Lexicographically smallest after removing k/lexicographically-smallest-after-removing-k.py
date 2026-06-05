class Solution:
    def lexicographicallySmallest(self, s, k):
        # code here
        n = len(s)
        if n&(n-1)==0:
            k = k//2
        else:
            k = k*2
        if k>=n:
            return "-1"
        
        stk=[]
        for i in s:
            while stk and k!=0 and stk[-1]>i:
                stk.pop()
                k-=1
            stk.append(i)
        while k:
            stk.pop()
            k-=1
        return ''.join(stk) if k==0 else "-1"