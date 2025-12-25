class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        d = 0
        once = True 
        arr.sort()

        for i in range(len(arr)-1):
            if once:
                d = abs(arr[i] - arr[i+1])
                once = False
            if abs(arr[i] - arr[i+1]) != d:
                return False
        return True
        