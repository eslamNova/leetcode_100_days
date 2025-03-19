from typing import List

class Solution:
    DEBUG = False  # Set this to False to disable debug prints

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the input list
        
        if self.DEBUG:
            print(f"Initial nums: {nums}")
            print(f"Initial sum: {sum(nums)}, Length: {n}")
        
        # If all elements are 1 from the start, no operations are needed
        if sum(nums) == n:
            return 0 
        
        op = 0  # Counter for the number of operations performed
        
        # Iterate through the array, considering every consecutive subarray of size 3
        for i in range(n - 3 + 1):
            
            if self.DEBUG:
                print(f"Checking subarray nums[{i}:{i+3}] -> {nums[i:i+3]}")
            
            if nums[i] == 0:
                op += 1  # Increment operation count
                
                if self.DEBUG:
                    print(f"Flipping first {3} elements (before flip): {nums}")
                
                # Flip the first (i+3) elements in the array
                for j in range(i, i+3):
                    nums[j] = 1 if nums[j] == 0 else 0
                
                if self.DEBUG:
                    print(f"After flip: {nums}")
                    print(f"Operations count: {op}")
        
        # Final check if all elements are 1
        if self.DEBUG:
            print(f"Final nums: {nums}")
            print(f"Final sum: {sum(nums)}")
            print(f"Total operations: {op}")
        
        if sum(nums) == n:
            return op
        else:
            return -1  # Return -1 if it is not possible to achieve all 1s

"""
Feedback on the solution above:

1. Time Complexity: O(n²) because for each position i, we're doing up to 3 flips, making it inefficient for large inputs.
2. The algorithm is using a greedy approach, which works for this problem but could be implemented more efficiently.
3. The debug prints are good for understanding the algorithm but can slow down execution.
4. The algorithm only checks the status of the first element (nums[i]) to decide if flipping is needed, which is correct
   for this greedy approach, but might be confusing without explanation.
5. The algorithm doesn't handle edge cases where array length is less than 3.

Below is a more optimized solution.
"""

class OptimizedSolution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge case: if array length is less than 3
        if n < 3:
            # For arrays of length 1 or 2, check if all elements are already 1
            return 0 if sum(nums) == n else -1
            
        # Create a copy to avoid modifying the input array
        working_nums = nums.copy()
        operations = 0
        
        # Greedy approach: fix the array from left to right
        for i in range(n - 2):
            if working_nums[i] == 0:
                # Need to flip this element and the next two
                operations += 1
                # Toggle the three elements
                for j in range(3):
                    if i + j < n:  # Ensure we don't go out of bounds
                        working_nums[i + j] ^= 1  # XOR with 1 to flip 0->1 or 1->0
            
        # Check if the last two elements are both 1
        if working_nums[-2:] != [1, 1]:
            return -1
            
        return operations

"""
Even more explicit O(N) solution without nested loops:
"""

class LinearSolution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge case handling
        if n < 3:
            return 0 if sum(nums) == n else -1
        
        # Create a copy of the array
        arr = nums.copy()
        operations = 0
        
        # Process elements left to right
        for i in range(n - 2):
            if arr[i] == 0:
                # Flip this and next two elements
                operations += 1
                
                # Directly flip without a loop
                arr[i] ^= 1
                arr[i+1] ^= 1
                arr[i+2] ^= 1
        
        # Check if we succeeded (all elements should be 1)
        return operations if arr[n-2] == 1 and arr[n-1] == 1 else -1
