# O(N)
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = list(sentence.split(" "))
        for i in range(len(l)):
            if l[i].startswith(searchWord):
                return i + 1
        return -1
        

        