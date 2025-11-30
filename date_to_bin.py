class Solution:
    def convertDateToBinary(self, date: str) -> str:

        sl = date.split("-")

        a = ""

        for n in sl:
            a += bin(int(n))[2:]
            a += "-"
        return a[:len(a)-1]        