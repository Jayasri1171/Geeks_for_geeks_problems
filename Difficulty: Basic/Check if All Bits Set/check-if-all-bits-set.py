class Solution:
    def isBitSet(self, n):
        # code here
        z=bin(n)
        z=z[2:]
        for i in z:
            if i!='1':
                return False
        return True