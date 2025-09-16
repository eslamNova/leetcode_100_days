class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        arr = text.split(" ")
        for w in arr:
            # print(w)
            for n in brokenLetters:
                if n in w:
                    ans += 1
                    # print(w)
                    # print(n)
                    break
            
        return len(arr) - ans
        