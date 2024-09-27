# O(1)ForSet,O(LogN)ForGet

class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        values = self.dic.get(key, [])
        l,r = 0, len(values) - 1

        while l <= r:
            m = (l+r) >> 1
            if values[m][1] <= timestamp:
                l = m + 1
                res = values[m][0]
            else:
                r = m - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
