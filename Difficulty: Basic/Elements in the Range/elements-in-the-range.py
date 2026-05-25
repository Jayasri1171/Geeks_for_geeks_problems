class Solution:
    def checkElements(self, start, end, arr):
        # code here
        arr.sort()
        if start in arr:
            z=arr.index(start)
        else:
            return False
        i=z
        chk=start
        while(True):
            if(arr[i]==chk):
                i+=1
                chk+=1
                if chk>end:
                    return True
            else:
                return False
            
        return False  
        
