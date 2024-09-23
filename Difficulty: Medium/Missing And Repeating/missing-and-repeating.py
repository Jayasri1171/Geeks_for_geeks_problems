#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        l=[]
        arr.sort()
        d={}
        for i in range(len(arr)):
            # print(i)
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                l.append(arr[i])
                break
        arr=list(set(arr))
        z=0
        for i in range(len(arr)):
            if i+1!=arr[i]:
                l.append(i+1)
                z=1
                break
        if z==0:
            l.append(len(arr)+1)
        return l
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends