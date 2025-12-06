class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        sor = sorted(score)[::-1]
        ans = []
        for s in score:
            i = sor.index(s)
            if i == 0:
                ans.append("Gold Medal")
            elif i == 1:
                ans.append("Silver Medal")
            elif i == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(i+1))

        return ans



        