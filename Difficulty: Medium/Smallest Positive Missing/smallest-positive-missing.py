class Solution:
    def missingNumber(self, arr):
        # code here
        arr.sort()
        for i in range(len(arr)):
            if arr[i]>0:
                arr=arr[i::]
                break
        
        arr=list(set(arr))
        arr.sort()
        i=1
        j=0
        while(True):
            if(arr[j]!=i):
                return i
            i+=1
            j+=1
            if(j==len(arr)):
                return i
        return i