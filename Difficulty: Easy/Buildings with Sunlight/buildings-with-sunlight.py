class Solution:
    def visibleBuildings(self, arr):
        # code here
        ans=0
        chkvar=0
        for i in arr:
            if i>=chkvar:
                ans+=1
                chkvar=i
        return ans