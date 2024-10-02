#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

# from typing import List


class Solution:
    def rotateDelete(self,  arr):
        i=0
        j=len(arr)//2
        while(j>0):
            # print(arr)
            z=arr[len(arr)-1]
            arr=arr[0:len(arr)-1]
            arr.insert(0,z)
            # print(arr)
            
            if(i>=len(arr)-1):
                i=0
                arr=arr[0:len(arr)-1]
            else:
                m=len(arr)-i-1
                arr=arr[0:m]+arr[m+1:len(arr)]
                # arr.remove(arr[m])
                i+=1
            # print(arr)
            j-=1
        # print(arr)
        return arr[0]
            
            
        



#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.rotateDelete(arr)
        print(res)
        t -= 1


# } Driver Code Ends