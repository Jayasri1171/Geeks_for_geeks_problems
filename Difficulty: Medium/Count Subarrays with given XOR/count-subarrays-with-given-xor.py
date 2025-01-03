class Solution:
    def subarrayXor(self, arr, k):
        # code here
        d={0:1}
        count=0
        summ=0
        for i in range(len(arr)):
            summ^=arr[i]
            if (summ^k) in d:
                count+=d[summ^k]
            if summ not in d:
                d[summ]=1
            else:
                d[summ]+=1
            
        return count

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends