class Solution:
    def URLify(self, s): 
        # code here
        ans=""
        for i in s:
            if i==" ":
                ans+="%20"
            else:
                ans+=i
        return ans
            
