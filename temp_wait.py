class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, idx = stack.pop()
                ans[idx] = (i - idx)
            stack.append([t,i])
        # for i in range(len(temperatures)):
        #     cur = temperatures[i]
        #     days = 0
        #     grt = False

        #     for j in range(i+1, len(temperatures)):
        #         days += 1
        #         if temperatures[j] > cur:
        #             grt = True
        #             break

        #     if not grt:
        #         days = 0
        #     ans.append(days)
        return ans
            
        