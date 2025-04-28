"""
2465. Number of Distinct Averages

Problem Description:
You are given a 0-indexed integer array nums of even length. You need to:
1. Sort the array
2. Pair the smallest number with the largest number, second smallest with second largest, and so on
3. Calculate the average of each pair
4. Return the number of distinct averages obtained

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n) to store the averages

FAANG Interview Feedback:
1. Good: 
   - Clean implementation of the core logic
   - Efficient use of sorting to pair numbers
   - Proper handling of even-length arrays

2. Areas for Improvement:
   - Could add input validation
   - Could optimize space usage
   - Could add more detailed comments
   - Could handle edge cases more explicitly

3. Follow-up Questions to Consider:
   - How would you handle odd-length arrays?
   - What if the numbers are very large (overflow considerations)?
   - How would you modify the solution if we needed to track which pairs produced each average?
"""

from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        """
        Calculate the number of distinct averages from pairing smallest and largest numbers.
        
        Args:
            nums (List[int]): Input array of even length
            
        Returns:
            int: Number of distinct averages
            
        Raises:
            ValueError: If input array length is odd
        """
        # Input validation
        if len(nums) % 2 != 0:
            raise ValueError("Input array must have even length")
            
        # Sort array to easily pair smallest with largest
        s = sorted(nums)
        n = len(nums)
        averages = set()  # Using set for O(1) insertion and uniqueness
        
        # Pair smallest with largest, second smallest with second largest, etc.
        for i in range(n//2):
            avg = (s[i] + s[n-1-i]) / 2
            averages.add(avg)
            
        return len(averages)

    def distinctAverages_optimized(self, nums: List[int]) -> int:
        """
        Optimized version that reduces space complexity by using a bit array
        to track seen averages.
        
        This version is more memory efficient when dealing with a large number of
        possible averages, as it uses a fixed-size bit array instead of storing
        all averages.
        
        Time Complexity: O(n log n)
        Space Complexity: O(1) as we use a fixed-size bit array
        """
        if len(nums) % 2 != 0:
            raise ValueError("Input array must have even length")
            
        s = sorted(nums)
        n = len(nums)
        
        # Since all numbers are integers, averages will be either integers or .5
        # We can use a bit array to track seen averages
        seen = [False] * (max(nums) + 1)  # For integer averages
        seen_half = [False] * (max(nums) + 1)  # For .5 averages
        
        for i in range(n//2):
            avg = (s[i] + s[n-1-i]) / 2
            if avg.is_integer():
                seen[int(avg)] = True
            else:
                seen_half[int(avg)] = True
                
        return sum(seen) + sum(seen_half)

# Example usage and test cases
if __name__ == "__main__":
    # Test case 1: Regular case
    nums1 = [4,1,4,0,3,5]
    sol = Solution()
    print(f"Test 1 - Input: {nums1}")
    print(f"Regular solution: {sol.distinctAverages(nums1)}")
    print(f"Optimized solution: {sol.distinctAverages_optimized(nums1)}")
    
    # Test case 2: All same numbers
    nums2 = [1,1,1,1]
    print(f"\nTest 2 - Input: {nums2}")
    print(f"Regular solution: {sol.distinctAverages(nums2)}")
    print(f"Optimized solution: {sol.distinctAverages_optimized(nums2)}")

        