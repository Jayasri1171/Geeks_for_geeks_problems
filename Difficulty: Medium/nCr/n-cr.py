#User function Template for python3
def sri(n):
    if(n<=1):
        return 1
    return (n*sri(n-1))
class Solution:
    def nCr(self, n, r):
        # code here
        return sri(n)//(sri(n-r)*sri(r))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends