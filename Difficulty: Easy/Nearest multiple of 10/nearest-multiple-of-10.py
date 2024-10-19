#User function Template for python3

class Solution:
    def roundToNearest (self, s) : 
        #Complete the function
        n=len(s)
        m=int(s[n-1])
        a=m%10
        check=0
        if(a==0):
            return s
        elif(a>5):
            check=1
            adding=10-a
        if(check==0):
            ss=list(s)
            ss[len(ss)-1]='0'
            b=""
            for i in ss:
                b+=i
            return b
        else:
            ss=list(s)
            carry=0
            for j in range(len(ss)-1,-1,-1):
                if(carry==0):
                    zz=int(int(ss[j])+adding)
                    if(zz==10):
                        carry=1
                    ss[j]='0'
                    
                else:
                    m=int(ss[j])
                    if(m+1==10):
                        count=1
                        ss[j]='0'
                    else:
                        ss[j]=str(m+1)
                        break
            ff=""
            for i in ss:
                ff+=i
            return ff
                
                
                
            
            
        
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends