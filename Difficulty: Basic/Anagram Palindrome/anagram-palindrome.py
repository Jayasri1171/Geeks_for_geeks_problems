class Solution:
    def canFormPalindrome(self, s):
        # code here
        chk=0
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]%2!=0:
                chk+=1
                if chk>1:
                    return False
        return True
                