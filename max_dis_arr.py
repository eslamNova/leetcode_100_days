# O(N)

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxi = arrays[0][-1]
        mini = arrays[0][0]
        maxd = 0 

        for i in range (1, len(arrays)):
            maxd = max(maxd, abs(mini - arrays[i][-1]), abs(maxi - arrays[i][0]))
            maxi = max(maxi, arrays[i][-1])
            mini = min(mini, arrays[i][0])

        return maxd
        
