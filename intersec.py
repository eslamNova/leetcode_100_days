class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        i,j = 0,0
        mi = []
        for n in event1:
            a,b = n.split(":")
            mi.append(int(a) * 60 + int(b))
        for n in event2:
            a,b = n.split(":")
            mi.append(int(a) * 60 + int(b))
        print(mi)
        if mi[0] <= mi[3] and mi[1] >= mi[2]:
            return True
        return False
    
# O(N)