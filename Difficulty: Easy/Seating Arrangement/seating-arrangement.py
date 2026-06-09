class Solution:
    def canSeatAllPeople(self, k, seats):
        # code here
        cnt=0
        onee=0
        if k>len(seats):
            return False
        if len(seats)<3:
            if seats==[0]:
                return True
            if seats==[0,0] and k<=1:
                return True
        for i in range(len(seats)):
            if i==0 or i==len(seats)-1:
                if seats[i]==0:
                    cnt+=2
            else:
                if seats[i]==0:
                    cnt+=1
                    onee=0
            if seats[i]==1:
                cnt=0
                if onee==1:
                    return False
                onee=1
                
            if cnt>=3:
                # print(i)
                k-=1
                cnt=1
        if k>0:
            return False
        return True