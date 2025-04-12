class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:

        # First generate all unique digit count patterns of k-palindromic numbers
        half_len = (n + 1) // 2
        digit_patterns = set()
        
        for num in range(10**(half_len - 1), 10**half_len):
            num_str = str(num)
            if n % 2 == 0:
                palindrome = num_str + num_str[::-1]
            else:
                palindrome = num_str + num_str[:-1][::-1]
            
            p_int = int(palindrome)
            if p_int % k == 0:
                # Store the sorted digits to identify unique patterns
                digit_pattern = tuple(sorted(palindrome))
                digit_patterns.add(digit_pattern)
        
        # Now count permutations for each unique digit pattern
        total = 0
        
        @lru_cache(maxsize=None)
        def count_valid_permutations(digits):
            counts = Counter(digits)
            length = len(digits)
            
            # Total permutations without restrictions
            denominator = 1
            for cnt in counts.values():
                denominator *= factorial(cnt)
            total_perms = factorial(length) // denominator
            
            # Subtract invalid permutations (starting with 0)
            if '0' in counts:
                if counts['0'] == length:  # All zeros
                    return 0
                invalid = factorial(length - 1)
                for d, cnt in counts.items():
                    if d == '0':
                        invalid = invalid * cnt // factorial(cnt)
                    else:
                        invalid //= factorial(cnt)
                total_perms -= invalid
            
            return total_perms
        
        for pattern in digit_patterns:
            total += count_valid_permutations(pattern)
        
        return total
        