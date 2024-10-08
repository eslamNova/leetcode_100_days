class Solution:
    def minSwaps(self, s: str) -> int:
        stack = deque()

        unbl = 0

        for ch in s:
            if ch == "[":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                
                else:
                    unbl += 1
        return (unbl + 1) // 2
