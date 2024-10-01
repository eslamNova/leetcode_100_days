from collections import defaultdict

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = defaultdict(int)
        
        # Count remainders of elements when divided by k
        for num in arr:
            remainder = num % k
            # Handle negative remainders to make them positive
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1
        
        # Now check if we can pair the elements
        for rem in remainder_count:
            # Special case for remainder 0: there must be an even number of such elements
            if rem == 0:
                if remainder_count[rem] % 2 != 0:
                    return False
            # Special case when rem == k / 2 (for even k), same logic as above
            elif rem * 2 == k:
                if remainder_count[rem] % 2 != 0:
                    return False
            else:
                # For other remainders, remainder_count[rem] must match remainder_count[k - rem]
                if remainder_count[rem] != remainder_count[k - rem]:
                    return False
        
        return True
