class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = []

        for e in emails:
            n = ""
            bef = True
            skip = False
            for c in e:
                if c == "@":
                    bef = False

                if bef:
                    if  c == ".":
                        continue
                    elif c == "+":
                        skip = True
                    elif not skip :
                        n += c
                else:
                    n += c

            if n not in ans:
                ans.append(n)
        return len(ans)

        