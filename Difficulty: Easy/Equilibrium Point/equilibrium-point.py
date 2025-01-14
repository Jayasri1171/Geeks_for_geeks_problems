# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        prefix=[]
        suffix=[]
        count=0
        for i in range(len(arr)):
            prefix.append(count)
            count+=arr[i]
        count=0
        for i in range(len(arr)-1,-1,-1):
            suffix.append(count)
            count+=arr[i]
        suffix=suffix[::-1]
        for i in range(len(arr)):
            if suffix[i]==prefix[i]:
                return i
        return -1




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends