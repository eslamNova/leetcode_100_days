from typing import List
from collections import Counter

class Solution:
    """
    A solution class for the Rabbit Groups problem.
    
    Problem Description:
    In a forest, each rabbit has some number of rabbits it claims to see (excluding itself).
    The answers array contains the number of rabbits each rabbit claims to see.
    We need to find the minimum number of rabbits that could be in the forest.
    
    Example:
    If answers = [1, 1, 2]
    - First rabbit says it sees 1 other rabbit
    - Second rabbit says it sees 1 other rabbit
    - Third rabbit says it sees 2 other rabbits
    Minimum possible rabbits = 5 (2 rabbits of color 1, 2 rabbits of color 2, 1 rabbit of color 3)
    """
    
    def numRabbits(self, answers: List[int]) -> int:
        """
        Calculate the minimum number of rabbits in the forest.
        
        Args:
            answers (List[int]): Array where answers[i] is the number of rabbits that 
                               the ith rabbit claims to see (excluding itself).
        
        Returns:
            int: The minimum number of rabbits that could be in the forest.
            
        Time Complexity: O(n) where n is the length of answers
        Space Complexity: O(n) to store the counter
        """
        # Count frequency of each answer
        c = Counter(answers)
        print(c)  # Debug print to see the distribution of answers
        
        ans = 0 
        # Iterate through each unique answer and its frequency
        for n in c:
            # g represents the group size (number of rabbits of same color)
            # For answer n, group size is n + 1 (including the rabbit itself)
            g = n + 1
            
            # clr represents the count of rabbits claiming to see n others
            clr = c[n]
            
            # Adjust the count to make it divisible by group size
            # This ensures we have complete groups of rabbits
            while clr % g != 0:
                clr += 1
                
            # Add the adjusted count to the total
            ans += clr
            
        return ans