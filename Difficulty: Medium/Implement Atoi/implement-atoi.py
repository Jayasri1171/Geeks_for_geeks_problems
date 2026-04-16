class Solution:
    def myAtoi(self, s):
        # code here
        ans=0
        chk=1
        digi="0123456789"
        tmp=0
        for i in range(len(s)):
            if s[i]=="+" or s[i]=="-" or s[i] in digi:
                if s[i] in digi:
                    tmp=i
                else:
                    tmp=i+1
                if s[i]=="-":
                    chk=-1
                break
        for i in range(tmp,len(s)):
            if s[i] not in digi:
                break
            ans=ans*10+int(s[i])
            if(ans>=2147483647):
                if chk==-1:
                    return  -2147483648
                else:
                    return 2147483647
            
        if chk==-1:
            return -1*ans
        return ans