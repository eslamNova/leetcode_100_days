class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        l,r = 0,0
        cut = False
        for i in s:
            if i == "1" and l == 0:
                if cut:
                    return False
                l = 1
            
            elif l == 1 and i == "1":
                r = 1

            elif l == 1 and i == "0":
                l = 0
                r = 0 
                cut = True
                

            print(l,r)

        return (l == r) or (l == 1 and len(s) == 1)
            





        