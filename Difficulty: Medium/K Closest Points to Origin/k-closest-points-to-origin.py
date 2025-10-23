class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        d={}
        for i in range(len(points)):
            z=(points[i][0]**2)+(points[i][1]**2)
            if z not in d:
                d[z]=[points[i]]
            else:
                d[z].append(points[i])
        m=dict(sorted(d.items(), key=lambda item: item[0]))
        count=0
        ans=[]
        check=0
        # print(m)
        for i in m:
            s=m[i]
            s.sort()
            for j in range(len(s)):
                ans.append(s[j])
                count+=1
                if(count==k):
                    check=1
                    break
            if check==1:
                break
            
        # print(m)
        return ans
