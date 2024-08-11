# O(NLOGN)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleet = list(zip(position, speed))

        fleet = sorted(fleet, key=lambda x: x[0])

        stack = []
        for p,s in fleet[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
