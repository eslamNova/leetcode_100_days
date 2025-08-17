class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        seen = set()
        for i, c in enumerate(password):
            if i > 0 and c == password[i - 1]:
                return False
            if c.isupper():
                seen.add('u')
            elif c.islower():
                seen.add('l')
            elif c.isdigit():
                seen.add('d')             
            else:
                seen.add('s')
        return  len(password) > 7 and len(seen) == 4
        
        #