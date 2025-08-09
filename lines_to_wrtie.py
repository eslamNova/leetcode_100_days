class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        a = "abcdefghijklmnopqrstuvwxyz"
        d = dict(zip(a, widths))
        # print(d)
        lines = 0
        c = 0
        for l in s:
            if c + d[l] <= 100:
                c += d[l]
            else:
                # print("NEW LINE")
                # print(l)
                # print(c)
                lines += 1
                c = d[l]

        return [lines+1,c]


        