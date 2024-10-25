class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        n=len(arr)
        if(n%2==0):
            sm=arr[0:n//2+1]
            la=arr[n-1:n//2-1:-1]
        else:
            sm=arr[0:n//2+2]
            la=arr[n-1:n//2:-1]
        qw=[]
        for j in range(n//2):
            qw.append(la[j])
            qw.append(sm[j])
        if(n%2!=0):
            qw.append(arr[n//2])
        return qw
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends