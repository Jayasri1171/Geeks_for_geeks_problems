#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        # arr=list(set(arr))
        first=0
        last=len(arr)-1
        ans=0
        while(first<last):
            if arr[first]+arr[last]==target:
                if arr[first]!=arr[last]:
                    ans+=d[arr[last]]*d[arr[first]]
                    first+=d[arr[first]]
                    last-=d[arr[last]]
                else:
                    ans+=(d[arr[first]]*(d[arr[first]]-1))//2
                    first+=d[arr[first]]
                    last-=d[arr[last]]
            elif arr[first]+arr[last]<target:
                first+=1
            else:
                last-=1
        return ans
                
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends