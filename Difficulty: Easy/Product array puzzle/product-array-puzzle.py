#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        pro=1
        zerocount=0
        for i in arr:
            if i!=0:
                pro*=i
            else:
                zerocount+=1
        ans=[]
        for i in range(len(arr)):
            if arr[i]!=0:
                if zerocount==0:
                    ans.append(pro//arr[i])
                else:
                    ans.append(0)
            else:
                if zerocount==1:
                    ans.append(pro)
                else:
                    ans.append(0)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends