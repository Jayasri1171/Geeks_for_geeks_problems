class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        # code here
        stk=[]
        for i in arr:
            if stk and ((stk[-1]>=0 and i<0) or (stk[-1]<0 and i>=0)):
                stk.pop()
            else:
                stk.append(i)
        return stk
                
            
            