# O(N∗Logn)

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        ans = [] 
        tmp = []

        for n in nums:
            ls = list(str(n))
            new = ''
            for l in ls:
                new += str(mapping[int(l)])
            
            tmp.append((int(new), n))


        for j in sorted(tmp, key = lambda x: x[0]):
            ans.append(j[1])

        return ans
        