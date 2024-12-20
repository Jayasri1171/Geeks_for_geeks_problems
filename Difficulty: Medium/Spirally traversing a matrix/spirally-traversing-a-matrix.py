class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        l=[]
        n=len(mat)
        m=len(mat[0])
        top=0
        down=n-1
        left=0
        right=m-1
        dir=0
        while(top<=down and left<=right):
            if(dir==0):
                for i in range(left,right+1):
                    l.append(mat[top][i])
                top+=1
            elif(dir==1):
                for i in range(top,down+1):
                    l.append(mat[i][right])
                right-=1
            elif(dir==2):
                for i in range(right,left-1,-1):
                    l.append(mat[down][i])
                down-=1
            else:
                for i in range(down,top-1,-1):
                    l.append(mat[i][left])
                left+=1
            dir=(dir+1)%4
        return l


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends