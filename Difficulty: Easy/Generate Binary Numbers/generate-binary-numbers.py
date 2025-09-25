class Solution:
    def generateBinary(self, n):
        # code here
        ans=[]
        for i in range(1,n+1):
            s=bin(i)
            s=s[2::]
            ans.append(s)
        return ans
        