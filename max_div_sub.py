from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Find the largest subset of integers where every pair of elements is divisible by each other.
        
        A divisible subset is one where for any two numbers a and b in the subset, either a % b == 0 or b % a == 0.
        
        Args:
            nums: List[int] - A list of distinct positive integers
            
        Returns:
            List[int] - The largest divisible subset of nums (any valid subset if multiple exist)
            
        Time Complexity: O(n²) where n is the length of nums
        Space Complexity: O(n) for storing the subsets
        
        Example:
            Input: nums = [1, 2, 3, 4, 8]
            Output: [1, 2, 4, 8]
            
            For subset [1, 2, 4, 8], all pairs are divisible:
            - 8 % 4 == 0
            - 8 % 2 == 0
            - 8 % 1 == 0
            - 4 % 2 == 0
            - 4 % 1 == 0
            - 2 % 1 == 0
        """
        # Initialize dictionary S with a key -1 mapping to an empty set
        # -1 is used as a starting point since any number is divisible by it
        S = {-1: set()}
        
        # Sort the input array to ensure we process smaller numbers first
        # This is critical because if a divides b, then a must be smaller than b
        sorted_nums = sorted(nums)
        
        # Example simulation with nums = [4, 8, 1, 2, 3]:
        # sorted_nums = [1, 2, 3, 4, 8]
        
        for x in sorted_nums:
            # For each number x, find the largest subset among all keys d where x is divisible by d
            # Then add x to this subset to form the new subset for key x
            # The max() function with key=len finds the subset with the maximum length
            # The | {x} operation adds x to the chosen subset
            
            # Example simulation:
            # When x = 1:
            #   S = {-1: set(), 1: {1}}
            
            # When x = 2:
            #   Candidates: S[-1] = set(), S[1] = {1} (since 2 % 1 == 0)
            #   Largest candidate: S[1] = {1}
            #   S[2] = {1, 2}
            #   S = {-1: set(), 1: {1}, 2: {1, 2}}
            
            # When x = 3:
            #   Candidates: S[-1] = set(), S[1] = {1} (since 3 % 1 == 0)
            #   Largest candidate: S[1] = {1}
            #   S[3] = {1, 3}
            #   S = {-1: set(), 1: {1}, 2: {1, 2}, 3: {1, 3}}
            
            # When x = 4:
            #   Candidates: S[-1] = set(), S[1] = {1}, S[2] = {1, 2} (since 4 % 1 == 0 and 4 % 2 == 0)
            #   Largest candidate: S[2] = {1, 2}
            #   S[4] = {1, 2, 4}
            #   S = {-1: set(), 1: {1}, 2: {1, 2}, 3: {1, 3}, 4: {1, 2, 4}}
            
            # When x = 8:
            #   Candidates: S[-1] = set(), S[1] = {1}, S[2] = {1, 2}, S[4] = {1, 2, 4}
            #   Largest candidate: S[4] = {1, 2, 4}
            #   S[8] = {1, 2, 4, 8}
            #   S = {-1: set(), 1: {1}, 2: {1, 2}, 3: {1, 3}, 4: {1, 2, 4}, 8: {1, 2, 4, 8}}
            
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
            
        # Return the largest subset found, converted to a list
        # This is the largest divisible subset where for any pair of elements, one divides the other
        # For the example: max(S.values(), key=len) = {1, 2, 4, 8}
        return list(max(S.values(), key=len))
        





        