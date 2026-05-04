class Solution:
    def isBinaryPalindrome(self, n):
        # code here
        z=bin(n)
        z=z[2:]
        m=z[::-1]
        if z==m:
            return True
        return False