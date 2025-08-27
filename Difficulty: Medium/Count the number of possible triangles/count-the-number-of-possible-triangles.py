#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        arr.sort()
        # print(arr)
        i=len(arr)-1
        count=0
        while(i>=2):
            start=0
            end=i-1
            while(start<end):
                if arr[start]+arr[end]>arr[i]:
                    count+=end-start
                    end-=1
                else:
                    start+=1
            i-=1
        return count
                


