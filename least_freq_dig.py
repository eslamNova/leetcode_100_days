class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:

        c = Counter(str(n))

        cc = c.most_common()

        lst = cc[-1][1]
        a = []
        # print(lst)
        for i in range(len(cc)):
            # print(cc[i])
            if cc[i][1] == lst:
                a.append(int(cc[i][0]))
                # print(a)
        # print(cc)

        return min(a)