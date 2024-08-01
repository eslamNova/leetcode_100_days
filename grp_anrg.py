# O(n*m)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}

        for s in strs:
            sort_s = str(sorted(s))

            if sort_s not in anag:
                anag[sort_s] = []

            anag[sort_s].append(s)
            
        return list(anag.values())