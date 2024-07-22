# O(N^2)
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = [] 
        tmp = heights.copy()
        for i in range(len(names)):
            m = max(tmp)
            n = heights.index(m)
            ans.append(names[n])
            tmp.remove(m)
        return ans


