    class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_groups = defaultdict(list)
        
        # Step 1: Group numbers by their sum of digits
        for num in nums:
            digit_sum = sum(int(d) for d in str(num))  # Compute digit sum
            digit_sum_groups[digit_sum].append(num)
        
        max_sum = -1  # Initialize result
        
        # Step 2: Process each group
        for group in digit_sum_groups.values():
            if len(group) > 1:  # Only consider groups with at least two numbers
                group.sort(reverse=True)  # Step 2: Sort in descending order
                max_sum = max(max_sum, group[0] + group[1])  # Take top two numbers
        
        return max_sum