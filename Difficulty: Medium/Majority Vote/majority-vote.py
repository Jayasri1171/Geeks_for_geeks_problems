class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        #Your Code goes here.
        n=len(nums)
        d={}
        l=[]
        z=n//3
        for i in nums:
            if i not in d:
                d[i]=1
                if z==0:
                    l.append(i)
            else:
                d[i]+=1
                if d[i]>z and i not in l:
                    l.append(i)
        if l==[]:
            return [-1]
        l.sort()
        return l
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends