#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        positive=[]
        negative=[]
        for i in arr:
            if i<0:
                negative.append(i)
            else:
                positive.append(i)
        z=[]
        i=0
        j=0
        while(i<len(positive) and j<len(negative)):
            z.append(positive[i])
            z.append(negative[j])
            i+=1
            j+=1
        if i<len(positive):
            while(i<len(positive)):
                z.append(positive[i])
                i+=1
        if j<len(negative):
            while(j<len(negative)):
                z.append(negative[j])
                j+=1
        # arr=[]
        while(arr):
            arr.pop()
        for i in z:
            arr.append(i)
        # return z
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends