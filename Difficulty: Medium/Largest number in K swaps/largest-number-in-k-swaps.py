#User function Template for python3

class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self, s, k):
        #code here
        l=list(s)
        ll=[]
        for i in l:
            ll.append(int(i))
        count=0
        i=0
        while(count<k and i<len(ll)-1):
            z=ll[i]
            ch=ll[i+1:]
            # print(ch)
            m=max(ch)
            # mm=ch.index(m)+i+1
            # print(mm)
            for j in range(len(ch)-1,-1,-1):
                if ch[j]==m:
                    mm=j+i+1
                    break
            if(m>z):
                ll[i]=m
                ll[mm]=z
                count+=1
            i+=1
            # print(ll,mm,i,count,ll[i])
        ans=""
        for i in ll:
            ans+=str(i)
        return ans
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob = Solution()
        print(ob.findMaximumNum(s, k))

        print("~")

# } Driver Code Ends