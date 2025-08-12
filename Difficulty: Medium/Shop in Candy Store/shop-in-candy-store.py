class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        minn = 0
        maxx = 0
        prices.sort()
        i=0
        j=len(prices)-1
        while(i<=j):
            minn+=prices[i]
            j=j-k
            i+=1
        ii=len(prices)-1
        jj=0
        while(ii>=jj):
            maxx+=prices[ii]
            jj=jj+k
            ii-=1
        l=[minn,maxx]
        return l
        