class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = []
        i = 0 
        for r in mat:
            c = Counter(r)
            ans.append([i, c[1]])
            i += 1
        
        # print(ans)
        return max(ans, key=lambda x: x[1])