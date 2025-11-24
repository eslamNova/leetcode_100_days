class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        ans = [] 
        current = 0
        for b in nums:

            current = (current * 2 + b) % 5
            if current == 0:
                ans.append(True)
            else:
                ans.append(False)

        return ans
        