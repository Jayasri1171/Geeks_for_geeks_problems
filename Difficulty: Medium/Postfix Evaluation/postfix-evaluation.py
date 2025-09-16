class Solution:
    
    def evaluatePostfix(self, arr):
        def is_number(i):
            try:
                float(i)   # int() would fail for "3.14", so float() is safer
                return True
            except ValueError:
                return False
        # code here
        chk='1234567890-'
        ans=0
        l=[]
        for i in arr:
            
            if is_number(i):
                l.append(int(i))
            else:
                z=l[-2]
                m=l[-1]
                l=l[0:len(l)-2]
                if i=="+":
                    l.append(z+m)
                elif i=='-':
                    l.append(z-m)
                elif i=='*':
                    l.append(z*m)
                elif i=='/':
                    l.append(z//m)
                else:
                    l.append(z**m)
            # print(l)
        return l[0]
                
                
        