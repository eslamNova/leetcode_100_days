# O(NLOGN)

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        num = []

        
        for t in timePoints:
            num.append((int(t.split(":")[0]) * 60 )+ int(t.split(":")[1]))

        num.sort()
        ans = min(num[i+1] - num[i] for i in range(len(num) - 1))
        

        return min(ans, 24 * 60 - num[-1] + num[0])
        