class Solution:
    def caseSort(self,s):
        #code here
        s=list(s)
        upper_case=[]
        lower_case=[]
        for i in s:
            if i.isupper():
                upper_case.append(i)
            else:
                lower_case.append(i)
        upper_case.sort()
        lower_case.sort()
        i=0
        j=0
        ij=0
        ans=""
        while(ij<len(s)):
            if s[ij].isupper():
                ans+=upper_case[i]
                i+=1
            else:
                ans+=lower_case[j]
                j+=1
            ij+=1
        return ans
        