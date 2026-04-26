class Solution:
    def commonElements(self, a, b, c):
        # code here
        m= list(set(a) & set(b) & set(c))
        m.sort()
        return m