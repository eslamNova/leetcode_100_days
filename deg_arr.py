class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c = Counter(nums)
        # print(c)
        deg = c.most_common()[0][1]
        ar = []
        for n in c:
            if c[n] == deg:
                ar.append(n)

        
        sp = 0 
        cnt = 0 
        spa = []
        for a in ar: # deg, 

            for i in nums:
                if i == a and sp == 0:
                    cnt += 1
                    sp += 1
                elif i == a and sp > 0:
                    sp += 1
                    cnt += 1
                elif i != a and sp > 0:
                    sp += 1

                if cnt == deg:
                    break
            spa.append(sp)
            sp = 0
            cnt = 0

        return min(spa)