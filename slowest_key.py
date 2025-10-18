class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        d = {}
        last = 0
        for i in range(len(keysPressed)):
            if keysPressed[i] not in d:
                d[keysPressed[i]] = 0
            if i > 0:
                last = releaseTimes[i-1]
            d[keysPressed[i]] = max(releaseTimes[i] - last, d[keysPressed[i]])
        max_val = max(d.values())
        max_keys = [j for j, v in d.items() if v == max_val]
        return max(max_keys)
        