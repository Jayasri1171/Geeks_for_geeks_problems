class Solution:
    
    def maxSum(self, n):
        # code here
        a=n//2
        b=n//3
        c=n//4
        if(a+b+c<=n):
            return n
        return (self.maxSum(a)+self.maxSum(b) +self.maxSum(c))
        
                
        
        
            
            