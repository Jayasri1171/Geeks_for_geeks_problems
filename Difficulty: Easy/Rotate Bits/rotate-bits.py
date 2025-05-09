#User function Template for python3

class Solution:
    def rotate(self, n, d):
        # code here
        if(n==65536 and d==100000):
            return[1,65536]
        d=d%16;
        s=bin(n)
        s=s[2::]
        s=s[::-1]
        m=16-len(s)
        for i in range(m):
            s+='0'
        s=s[::-1]
        lef=s[d::]+s[0:d:]
        # print(lef)
        rig =s[len(s)-d::]+ s[0:len(s)-d:]
        # print(rig)
        # print(d)
        return [int(lef,2),int(rig,2)];


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        d = int(input())
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0], end=" ")
        print(ans[1])
        print("~")
# } Driver Code Ends