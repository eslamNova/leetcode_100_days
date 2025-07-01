class Solution:
    def possibleStringCount(self, word: str) -> int:
        groups = []
        curr_char = word[0]
        count = 1
        
        for i in range(1, len(word)):
            if word[i] == curr_char:
                count += 1
            else:
                groups.append(count)
                curr_char = word[i]
                count = 1
        
        groups.append(count) 
        
        total = 1 
        for g in groups:
            if g >= 2:
                total += g - 1
        
        return total

        