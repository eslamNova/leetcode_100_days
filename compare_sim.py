# O(N3)
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        ans = 0

        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if i < j < k:
                        if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            ans += 1
        return ans