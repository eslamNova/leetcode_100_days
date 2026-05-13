class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        s = []
        for i in range(1,n+1):
            s.append(i)
        print(s)
        ans = []
        ps, pp = "Push", "Pop"        
        i,j = 0,0
        tl = len(target)
        while j < tl:
            if target[j] == s[i]:
                ans.append(ps)
                j += 1
                i += 1
            else:
                ans.append(ps)
                ans.append(pp)
                i += 1
        return ans


