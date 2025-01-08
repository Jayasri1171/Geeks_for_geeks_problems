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
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends