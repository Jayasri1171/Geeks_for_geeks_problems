#User function Template for python3
class Solution:
	def isDivisible(self, s):
		# code here
		z=int(s,2)
		if(z%3==0):
		    return True
		return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ob = Solution()
        ans = ob.isDivisible(s)

        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends