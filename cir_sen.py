# O(N)

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        t = ""
        first = True
        for w in sentence.split(" "):
            if first:
                t = w[-1]
                first = False
            else:
                if w[0] != t:
                    return False
                t = w[-1]
        return True

        