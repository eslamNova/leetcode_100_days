class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        ev = []

        for n in nums:
            if n % 2 == 0:
                ev.append(n)
        if not ev:
            return -1
        
        return sorted(Counter(ev).items(), key=lambda x: (-x[1], x[0]))[0][0]