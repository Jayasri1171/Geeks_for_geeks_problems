# Structure of binary tree node
'''
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
'''

class Solution:
    def sri(self,root,d,pos):
        if(root==None):
            return 
        if pos not in d:
            d[pos]=root.data
        else:
            d[pos]+=root.data
        self.sri(root.left,d,pos-1)
        self.sri(root.right,d,pos+1)
    def verticalSum(self, root):
        # code here
        d={}
        self.sri(root,d,0)
        s=dict(sorted(d.items()))
        ans=[]
        for i in s:
            ans.append(s[i])
        return ans
        