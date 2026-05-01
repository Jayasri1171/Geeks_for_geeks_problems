import heapq
class Solution:
    def kthLargest(self, arr, n):
        # code here 
        heap=[]
        ans=[]
        for i in range(len(arr)):
            if(len(heap)<n):
                heapq.heappush(heap, arr[i])
            else:
                if(arr[i]>=heap[0]):
                    heapq.heappop(heap)
                    heapq.heappush(heap,arr[i])
            if(len(heap)==n):
                ans.append(heap[0])
            else:
                ans.append(-1)
        return ans