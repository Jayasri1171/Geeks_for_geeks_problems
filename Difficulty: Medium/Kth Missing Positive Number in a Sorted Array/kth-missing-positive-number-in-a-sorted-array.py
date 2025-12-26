class Solution:
    def kthMissing(self, arr, k):
        # code here
        i=1
        j=0
        kcnt=0
        while(j<len(arr)):
            if i==arr[j]:
                i+=1
                j+=1
            else:
                kcnt+=1
                i+=1
                if kcnt==k:
                    return i-1
        return j+k
                