class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # Helper function for DFS with memoization
        def dfs(start, seen):
            if start == len(s):  # If we reach the end, no more splits can be made
                return 0
            
            # Variable to store the maximum number of unique splits
            max_splits = 0
            
            # Explore all possible substrings starting from index `start`
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                
                # If the substring is unique, we add it to the set and explore further
                if substring not in seen:
                    seen.add(substring)  # Mark this substring as used
                    max_splits = max(max_splits, 1 + dfs(end, seen))  # Add 1 for this split and recurse
                    seen.remove(substring)  # Backtrack to try other splits
            
            return max_splits
        
        # Start the DFS from the beginning of the string with an empty set
        return dfs(0, set())