class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        a = 0 

        for n in patterns:
            if n in word:
                a += 1
        return a
        