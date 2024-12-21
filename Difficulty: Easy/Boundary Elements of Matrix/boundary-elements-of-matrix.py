#User function Template for python3

class Solution:
	def BoundaryElements(self, mat):
		# Code here
		l=[]
		for i in range(len(mat)):
		    for j in range(len(mat)):
		        if(i==0 or i==len(mat)-1 or j==0 or j==len(mat)-1):
		            l.append(mat[i][j])
		return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		ob = Solution()
		ans = ob.BoundaryElements(matrix)
		for _ in ans:
			print(_ ,end = " ")
		print()

# } Driver Code Ends