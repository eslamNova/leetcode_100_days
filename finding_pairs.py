class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):

        self.nums1 = nums1
        self.nums2 = nums2
        self.counter = Counter(self.nums2)
        

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        
        # Update nums2
        self.nums2[index] = new_val
        
        # Update frequency map
        self.counter[old_val] -= 1
        if self.counter[old_val] == 0:
            del self.counter[old_val]
        self.counter[new_val] += 1
        

    def count(self, tot: int) -> int:
        out = 0
        for n in self.nums1:
            out += self.counter.get(tot - n, 0)
        return out
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)