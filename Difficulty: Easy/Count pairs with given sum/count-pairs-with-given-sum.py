#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        arr.sort()
        d={}
        count=0
        for i in arr:
            if (target-i) in d:
                count+=d[target-i]
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return count
            

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends