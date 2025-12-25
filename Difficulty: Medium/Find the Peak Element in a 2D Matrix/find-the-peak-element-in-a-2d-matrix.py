class Solution:
    def findPeakGrid(self, mat):
        # code here
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                m=0
                if(i>0):
                    if(mat[i-1][j]<=mat[i][j]):
                        m+=1
                else:
                    m+=1
                if(j>0):
                    if(mat[i][j-1]<=mat[i][j]):
                        m+=1
                else:
                    m+=1
                if(i<len(mat)-1):
                    if(mat[i+1][j]<=mat[i][j]):
                        m+=1
                else:
                    m+=1
                if(j<len(mat[0])-1):
                    if(mat[i][j+1]<=mat[i][j]):
                        m+=1
                else:
                    m+=1
                if m==4:
                    return [i,j]
        return -1