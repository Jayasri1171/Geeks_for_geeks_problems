class Solution:
    def replaceElements(self, arr):
        # code here
        tmp1=arr[0]
        tmp2=arr[1]
        arr[0]=tmp1^tmp2
        i=1
        while(i<len(arr)-1):
            tmp2=arr[i]
            arr[i]=tmp1^arr[i+1]
            tmp1=tmp2
            i+=1
        z=len(arr)-1
        arr[z]=arr[z]^tmp1