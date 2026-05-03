class Solution:
    def sortBySetBitCount(self, arr):
        # code here
        d={}
        for i in arr:
            z=bin(i)
            m=z.count('1')
            if m not in d:
                d[m]=[i]
            else:
                d[m].append(i)
        sorted_dict = dict(sorted(d.items(),reverse=True))
        ans=[]
        for i in sorted_dict:
            ans+=sorted_dict[i]
        return ans
        
            