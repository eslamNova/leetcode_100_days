class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False
        
        stack = []
        dic = {")" : "(", "}" : "{" , "]" : "[" }
        
        for n in s:
            if n not in dic.keys():
                stack.append(n)
            elif not stack or dic[n] != stack.pop():
                return False
        return stack == []
