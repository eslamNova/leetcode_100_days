class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ts = text.split(" ")
        ans = []
        for i in range(len(ts)):
            if first == ts[i]:
                if i+1 < len(ts):
                    if second == ts[i+1]:
                        if i+2 < len(ts):
                            ans.append(ts[i+2])
        
        return ans

        