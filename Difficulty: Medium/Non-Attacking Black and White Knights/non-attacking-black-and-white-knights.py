class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        # code here
        ans=0
        
        for i in range(n):
            for j in range(m):
                ttl=n*m-1
                if(i-2>=0 and j-1>=0):
                    ttl-=1
                if(i-2>=0 and j+1<m):
                    ttl-=1
                if(i-1>=0 and j-2>=0):
                    ttl-=1
                if(i-1>=0 and j+2<m):
                    ttl-=1
                if(i+1<n and j-2>=0):
                    ttl-=1
                if(i+1<n and j+2<m):
                    ttl-=1
                if(i+2<n and j-1>=0):
                    ttl-=1
                if(i+2<n and j+1<m):
                    ttl-=1
                # print(ttl)
                ans+=ttl
        return ans
                