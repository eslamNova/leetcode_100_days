class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        z = [i for s in grid for i in s]

        for q in range(5):
            if q == 2 or q == 5:
                continue
            s = z[q] + z[q+1] + z[q+3] + z[q+4]
            c = Counter(s)
            # print(s)
            if c['W'] >= 3 or c['B'] >= 3:
                return True
            
        
        return False
            



        