class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0 
        for i in range(len(words)):
            
            for j in range(len(words)):
                if j > i:
                    if Counter(words[i]).keys() == Counter(words[j]).keys(): 
                        ans += 1
                    
        return ans
        