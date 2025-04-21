class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # ans = 0
        # for i in range(lower,upper+1,1):
        #     valid = True
        #     s = i
        #     for d in differences:
        #         if d + s < lower or d + s > upper:
        #             valid = False
        #             break 
        #         else:
        #             s = d + s

        #     if valid:
        #         ans += 1
        # return ans
        min_val = 0
        max_val = 0
        curr = 0

        for d in differences:
            curr += d
            min_val = min(min_val, curr)
            max_val = max(max_val, curr)

        # the valid starting values of arr[0] lie in this range:
        min_start = lower - min_val
        max_start = upper - max_val

        return max(0, max_start - min_start + 1)


        