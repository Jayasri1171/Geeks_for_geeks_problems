#User function Template for python3
from sortedcontainers import SortedDict
 
class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        z={}
        for i in d:
            if d[i] not in z:
                z[d[i]]=[i]*d[i]
            else:
                 z[d[i]]+=([i]*d[i])
        m=SortedDict(z)
        p=[]
        for i in m:
            x=m[i]
            x.sort()
            x=x[::-1]
            p+=x
        return p[::-1]
                
                
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):

        arr = list(map(int, input().strip().split()))
        l = Solution().sortByFreq(arr)
        print(*l)

# } Driver Code Ends