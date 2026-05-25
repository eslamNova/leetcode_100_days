class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)
        s = []

        for i in range(len(temperatures)):
            t = temperatures[i]
            if not s:
                s.append(i)
            else:
                while s and temperatures[i] > temperatures[s[-1]]:
                    ti = s.pop()
                    ans[ti] = i - ti    
                else:
                    s.append(i)
        return ans


        
