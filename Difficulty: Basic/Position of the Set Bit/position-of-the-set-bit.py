class Solution:
    def findPosition(self, n):
        # code here 
        s=bin(n)
        s=s[2:]
        z=s.count('1')
        if(z!=1):
            return -1
        return len(s)
            