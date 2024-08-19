# O(N)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = []

        l,r = 0, len(height)-1

        while l < r:
            a = min(height[l], height[r]) * (r-l)
            ans.append(a)

            if height[l] < height[r]:
                # print(height[l+1], height[l])
                l += 1
            else:
                # print(height[r-1], height[r])
                r -= 1
        
            # print(ans)
        
        return max(ans)

        