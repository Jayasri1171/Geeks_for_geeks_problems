class Solution:
	def topKFreq(self, arr, k):
		# Code here
		d={}
		for i in arr:
		    if i not in d:
		        d[i]=1
		    else:
		        d[i]+=1
	    dic = dict(sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True))
	   # print(dic)
	    ans=[]
	    temp=0
	    for i in dic:
	        ans.append(i)
	        temp+=1
	        if temp==k:
	            break
	        
	    return ans
		
		