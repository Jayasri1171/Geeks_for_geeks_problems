'''
Structure of linked list node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        # code here
        stk=[]
        tmp=head
        while(tmp):
            while(stk):
                if(stk[-1]<tmp.data):
                    stk.pop()
                else:
                    break
            stk.append(tmp.data)
            tmp=tmp.next
        ans=Node(stk[0])
        tmp1=ans
        for i in range(1,len(stk)):
            z=Node(stk[i])
            tmp1.next=z
            tmp1=tmp1.next
        return ans