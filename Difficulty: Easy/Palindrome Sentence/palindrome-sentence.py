class Solution:
	def isPalinSent(self, s):
		# code here
		check='qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890'
		m=[]
		for i in s:
		    if i in check:
		        if ord(i)>=65 and ord(i)<=90:
		            i=chr(ord(i)+32)
		        m.append(i)
	    n=m[::-1]
	   # print(n,m)
	    if n==m:
	        return True
	    return False