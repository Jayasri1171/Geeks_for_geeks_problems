class Solution:
    def removeSpaces(self, s):
        # code here
        ans=""
        for i in s:
            if i!=" ":
                ans+=i
        return ans