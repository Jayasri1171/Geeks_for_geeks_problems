class Solution:
	def maxSubstring(self, s):
		# code here
		ans = 0
		current = 0
		for i in s:
		    if i == '1':
		        current = max(0, current-1)
		    else:
		        current += 1
		    ans = max(ans, current)
		return ans if ans > 0 else -1
		