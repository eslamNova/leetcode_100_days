class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        sarr= str(arr)
        for i in range(len(arr)-m):
            print(arr[i:i+m])
            print(str(arr[i:i+m] * k)[1:-1])
            if str(arr[i:i+m] * k)[1:-1] in sarr:
                return True
        return False
        