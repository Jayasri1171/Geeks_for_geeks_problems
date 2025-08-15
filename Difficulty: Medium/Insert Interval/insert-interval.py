class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        ans=[]
        check=-1
        for i in range(len(intervals)):
            z=intervals[i]
            if(z[1]<newInterval[0]):
                ans.append(z)
            else:
                s=min(z[0],newInterval[0])
                for j in range(i,len(intervals)):
                    m=intervals[j]
                    if(newInterval[1]<m[0]):
                        ans.append([s,max(newInterval[1],intervals[j-1][1])])
                        check=j
                        break
                if check==-1:
                    check=len(intervals)
                    ans.append([s,max(newInterval[1],intervals[j][1])])
                break
        if(check==-1):
            ans.append(newInterval)
            return ans
        for j in range(check,len(intervals)):
            ans.append(intervals[j])
        return ans
                        
        