
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        pn = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if i == j or i == len(nums) - j - 1:
                    if nums[i][j] not in pn:
                        pn.append(nums[i][j])

        pn = sorted(pn)
        for i in range(len(pn)-1,-1,-1):
            n = pn[i]
            if n <= 1:
                break
            else:
                is_prime = True
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    return n

        return 0
        