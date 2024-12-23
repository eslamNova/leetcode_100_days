# O(N)
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        visited = []
        here = ""

        for p in paths:
            visited.append(p[0])
        
        for p in paths: # because it's sure that there is a valid path
            if p[1] not in visited:
                return p[1]