# O(K*N)
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        r= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        st = ""
        for n in s:
            st += str(r.index(n)+1)

        for i in range(k):    
            sm = 0
            for n in st:
                sm += int(n)
            
            st = str(sm)
        
        return int(st)
