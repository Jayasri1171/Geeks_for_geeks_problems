#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        for i in range(len(arr)):
            if arr[i]==key:
                return i
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends