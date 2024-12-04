#User function Template for python3

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        s1=list(s1)
        s2=list(s2)
        d={}
        m={}
        for i in s1:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in s2:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        if m!=d:
            return False
        for i in range(len(s1)):
            z=s1[0]
            s1.remove(s1[0])
            s1.append(z)
            if s1==s2:
                return True
        return False
            


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
    for i in range(t):
        s1 = str(input())
        s2 = str(input())
        if (Solution().areRotations(s1, s2)):
            print("true")
        else:
            print("false")

# } Driver Code Ends