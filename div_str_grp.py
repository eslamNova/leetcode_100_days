class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        r = len(s) % k
        print(len(s))
        print(r)
        n = 0
        if r > 0:
            n += 1
        n += len(s)//k
        ans = []
        i = 0
        while i <= n*k - k:
            # print(i)
            if i+k > len(s):
                print("HERE")
                ss = s[i:]
                ss += fill * (k-r)
                ans.append(ss)
                break
            ans.append(s[i:i+k])
            i += k
        return ans


        