class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        s = sum(nums)
        print(s)
        if s % 3 == 0:
            return s
        m1 = []
        m2 = [] 

        for n in nums:
            if n % 3 == 1:
                m1.append(n)
            elif n% 3 == 2:
                m2.append(n)

        m1.sort()
        m2.sort()

        if s % 3 == 1:
            o1 = float("inf")
            if len(m1) >= 1:
                o1 = m1[0]

            o2 = float("inf")
            if len(m2) >= 2:
                o2 = m2[0] + m2[1]
            
            rem = min(o1, o2)
            if rem == float("inf"):
                return 0 
            return s - rem
        if s % 3 == 2:
            o1 = float("inf")
            if len(m1) >= 2:
                o1 = m1[0] + m1[1]

            o2 = float("inf")
            if len(m2) >= 1:
                o2 = m2[0] 
            
            rem = min(o1, o2)
            if rem == float("inf"):
                return 0 
            return s - rem
        

        # ns = sorted(nums)
        # nss = s
        # i = 0
        # while nss > 0:
        #     t = nss - ns[i] 
        #     if t % 3 == 0:
        #         return t
        #     else:
        #         nss -= 
        # for i in ns:
        #     nss = s - i
        #     print(nss)
        #     if nss % 3 == 0:
        #         return nss
        # return 0 
        