class Solution:
    def calPoints(self, operations: List[str]) -> int:
        r = []
        s = 0 

        for n in operations:
            try:
                s = int(n)
            except:
                s = 0
                # print("NOT DIG")
            
            if s != 0:
                r.append(s)
            elif n == "C":
                r.pop(-1)
            elif n == "D":
                r.append(r[-1]*2)
            elif n == "+":
                r.append(r[-1] + r[-2])
            # print(r)
        return sum(r) 
        