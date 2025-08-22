class Solution:
    def median(self, mat):
    	# code here 
    	s=[]
    	for i in mat:
    	    for j in i:
    	        s.append(j)
        s.sort()
        return s[len(s)//2]
    	