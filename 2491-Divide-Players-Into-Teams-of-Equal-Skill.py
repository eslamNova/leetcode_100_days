from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total_sum = sum(skill)
        # Total sum should be divisible by the number of teams (n/2 teams)
        if total_sum % (n // 2) != 0:
            return -1
        
        # Each team must have this sum of skills
        target_sum = total_sum // (n // 2)
        
        skill.sort()  # Sort the skill list to make pairing easier
        ans = 0
        
        # Try pairing smallest with largest, second smallest with second largest, etc.
        for i in range(n // 2):
            if skill[i] + skill[n - i - 1] != target_sum:
                return -1
            # Add the product of the two skills
            ans += skill[i] * skill[n - i - 1]
        
        return ans
