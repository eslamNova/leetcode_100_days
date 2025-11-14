class Solution:
    def maxFreqSum(self, s: str) -> int:

        c = Counter(s)
        v = "aeiou"
        cm = c.most_common()
        # print(cm)
        vf = 0 
        cf = 0 
        vf_done = False
        cf_done = False
        for i in cm:
            if i[0] in v and not vf_done:
                vf = i[1]
                vf_done = True

            elif not cf_done and i[0] not in v:
                cf = i[1]
                cf_done = True
            elif cf_done and vf_done:
                break

        return vf + cf


        