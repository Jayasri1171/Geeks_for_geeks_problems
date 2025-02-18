#{ 
 # Driver Code Starts
#Initial Template for Python 3
from typing import List


# } Driver Code Ends
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

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        k = int(input())
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        
        solution = Solution()
        ans = solution.kClosest(points, k)
        ans.sort()
        for point in ans:
            print(point[0], point[1])
        print("~")

# } Driver Code Ends