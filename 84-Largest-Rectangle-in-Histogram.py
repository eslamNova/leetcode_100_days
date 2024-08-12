class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxAr = 0
        stack = [] 

        for i, h in enumerate(heights):
            s = i 
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxAr = max(maxAr, height * (i- index))

                s = index

            stack.append((s, h))
        for i, h in stack:
            maxAr = max(maxAr, h* (len(heights) - i))
        return maxAr
        