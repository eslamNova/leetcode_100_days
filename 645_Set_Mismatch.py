#Find the number that occurs twice and the number that is missing and return them in the form of an array.


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        d = Counter(nums)
        m = 0
        r = 0
        for i in range(1, len(nums)+1):
            if i not in nums:
                m = i
            if d[i] == 2:
                r = i
            if m != 0 and r != 0:
                break
                
        return [r,m]
