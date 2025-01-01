#User function Template for python3


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        d={}
        for i in range(len(arr)):
            m=arr[i]
            q={}
            for j in m:
                if j not in q:
                    q[j]=1
                else:
                    q[j]+=1
            q_tuple = tuple(sorted(q.items()))
            if q_tuple not in d:
                d[q_tuple] = [m]
            else:
                d[q_tuple].append(m)
        # print(d)
        l=[]
        for i in d:
            l.append(d[i])
        return l
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends