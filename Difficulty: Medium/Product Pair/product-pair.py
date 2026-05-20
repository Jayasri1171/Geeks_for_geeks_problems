class Solution:
    def isProduct(self, arr, target):
        # code here
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        if target==0:
            if 0 in d:
                return True
        for i in arr:
            if i!=0 and target!=0:
                if target//i in d and (target//i)*i==target:
                    if target//i == i:
                        if d[target//i]>1:
                            # print(i)
                            return True
                    else:
                        # print(i,target//i,"fghjk")
                        return True
        return False
                