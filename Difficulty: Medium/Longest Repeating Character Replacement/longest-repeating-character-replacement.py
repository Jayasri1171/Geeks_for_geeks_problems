class Solution:
    def longestSubstr(self, s, k):
        # Code here
        longest = 0
        l = 0
        chk = [0]*26
        for i in range(len(s)):
            chk[ord(s[i])-65]+=1
            while(i-l+1 - max(chk))>k:
                chk[ord(s[l])-65]-=1
                l+=1
            longest= max(longest, (i-l+1))
        return longest