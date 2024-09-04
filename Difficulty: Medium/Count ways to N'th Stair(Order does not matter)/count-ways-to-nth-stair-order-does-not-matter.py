#User function Template for python3

class Solution:
	def nthStair(self,n):
		# Code here
		count=0
		for i in range(n+1):
		    z=n-i
		    if(z%2)==0:
		        count+=1
	    return count
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthStair(n)
		print(ans)
# } Driver Code Ends