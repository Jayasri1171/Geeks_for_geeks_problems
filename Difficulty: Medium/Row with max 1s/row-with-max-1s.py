#User function Template for python3
class Solution:

    def rowWithMax1s(self,arr):
        count=len(arr[0])
        m=0
        count1=0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if(arr[i][j]==1):
                    count1=1
                    if(count>j):
                        count=j
                        m=i
                        break
        if count1==0:
            return -1
        return m
        # code here


