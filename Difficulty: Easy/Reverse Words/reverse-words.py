# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,str):
        # code here 
        g=''
        l=[]
        for i in range(len(str)):
            if str[i]!='.':
                g+=str[i]
            else:
                l.append(g)
                g=''
        l.append(g)
        k=''
        k+=l[len(l)-1]
        for j in range(len(l)-2,-1,-1):
            k+='.'
            k+=l[j]
            
        return k


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends