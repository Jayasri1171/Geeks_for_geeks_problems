class Solution:
    def divby13(self, s):
        # code here 
        ans=""
        for i in range(len(s)):
            ans+=s[i]
            # if(int(ans)%13<1):
            #     continue
            rem = int(ans)%13
            if(rem==0):
                ans=""
            else:
                ans=str(rem)
        # print(ans)
        if ans=="":
            return True
        return False