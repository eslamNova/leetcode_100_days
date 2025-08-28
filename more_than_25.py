class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        c = Counter(arr)

        for n in c:
            if c[n] > len(arr)//4:
                return n
                