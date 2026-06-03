class Solution:
    def freqInRange(self, arr, queries):
        # code here
        d={}
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=[i]
            else:
                d[arr[i]].append(i)
        ans=[]
        for i in range(len(queries)):
            z=queries[i]
            cnt=0
            if z[2] in d:
                s=d[z[2]]
                for k in range(len(s)):
                    if s[k]>=z[0] and s[k]<=z[1]:
                        cnt+=1
            ans.append(cnt)
        return ans
            