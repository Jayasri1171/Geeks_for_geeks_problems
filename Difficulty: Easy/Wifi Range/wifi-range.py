class Solution:
    def wifiRange(self, s, x):
        # code here
        i=0
        nowifi=0
        cvg=0
        while(i<len(s)):
            if s[i]=='1':
                cvg=x
                if(nowifi>cvg):
                    return False
                else:
                    nowifi=0
            else:
                nowifi+=1
                if(cvg>0):
                    nowifi-=1
                    cvg-=1
            i+=1
        if nowifi>0:
            return False
        return True
                
            