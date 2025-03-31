class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1
        
        s = [1, 2, 2]
        i = 2  # pointer to the current count
        next_num = 1  # next number to append (alternates between 1 and 2)
        
        while len(s) < n:
            count = s[i]
            s.extend([next_num] * count)
            next_num ^= 3  # alternates between 1 and 2 (1 ^ 3 = 2, 2 ^ 3 = 1)
            i += 1
        
        return s[:n].count(1)
        