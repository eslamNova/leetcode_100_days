# O(N2)

class Solution:
    def distinctIntegers(self, n: int) -> int:
        distinct_numbers = set()
        distinct_numbers.add(n)  # Start with the initial number n
        new_numbers = [n]  # List to process for the next day's numbers
        
        while new_numbers:
            current_numbers = new_numbers
            new_numbers = []  # Prepare for new numbers to be added
            
            for x in current_numbers:
                # Calculate all divisors of (x - 1)
                for i in range(1, x):
                    if x % i == 1:
                        if i not in distinct_numbers:
                            distinct_numbers.add(i)
                            new_numbers.append(i)  # Only add new numbers

        return len(distinct_numbers)