class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        
        total = sum(arr)
        if total % 3 != 0:
            return False

        target = total // 3
        a = 0
        c = 0
        for i in arr:
            a += i
            if a == target:
                a = 0
                c += 1
        return c >= 3
        