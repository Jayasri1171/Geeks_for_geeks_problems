#User function Template for python3

class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,mat):
        # code here 
        top=0
        bottom=len(mat)-1
        left=0
        right=len(mat[0])-1
        dir=0
        l=[]
        while(dir<4):
            if(dir==0):
                for i in range(left,right+1):
                    l.append(mat[top][i])
                top+=1
            if(dir==1):
                for i in range(top,bottom+1):
                    l.append(mat[i][right])
                right-=1
            if(dir==2):
                for i in range(right,left-1,-1):
                    l.append(mat[bottom][i])
                bottom-=1
            if(dir==3):
                for i in range(bottom,top-1,-1):
                    l.append(mat[i][left])
                left+=1
            dir+=1
        return l
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        r = int(input())
        c = int(input())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t = [int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j] = t[j]
        ans = ob.BoundaryTraversal(matrix)
        print(*ans)
        print("~")

# } Driver Code Ends