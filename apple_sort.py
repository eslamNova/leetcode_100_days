class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        ta = sum(apple)
        co = sorted(capacity)[::-1]

        a = 0  
        i = 0

        while a < ta:
            a += co[i]
            i += 1
        return i