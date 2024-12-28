class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        while k > 0:
            m = max(gifts)
            gifts.remove(m)
            mr = int(math.sqrt(m))
            gifts.append(mr)
        
            k -= 1
        return sum(gifts)

        