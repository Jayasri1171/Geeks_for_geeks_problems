#User function Template for python3

class Solution:
    def findMissing(self, arr):
        # code here
        m=arr[0];
        d=arr[1]-arr[0];
        ch=arr[0];
        for i in arr:
            if ch!=i:
                return ch
            ch=ch+d
        return ch
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
import math


def main():
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    solution = Solution()

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        print(solution.findMissing(arr))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends