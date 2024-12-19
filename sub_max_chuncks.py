# O(N)
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        c = 0
        m = -11

        for i in range(len(arr)):
          maxi = max(m, arr[i])
          m = maxi
          if maxi == i:
            c += 1
        return c  