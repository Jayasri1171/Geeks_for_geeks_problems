class Solution:
    def countAndSay(self, n):
        # code here
        l=["1"]
        for i in range(1,31):
            z=l[i-1]
            z=list(z)
            m=z[0]
            count=1
            s=""
            if(len(z)==1):
                l.append('11')
            else:
                for j in range(1,len(z)):
                    if z[j]==m:
                        count+=1
                    else:
                        s+=(str(count)+m)
                        m=z[j]
                        count=1
                s+=(str(count)+m)
                l.append(s)
        qw=l[n-1]
        return qw
            
                    
                
                
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countAndSay(n))

        print("~")
# } Driver Code Ends