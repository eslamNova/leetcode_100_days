class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        target = {}
        for i in range(len(nums)-1):
            if nums[i] == key:
                if nums[i+1] not in target:
                    target[nums[i+1]] = 1
                else:
                    target[nums[i+1]] += 1
        # print(target)
        # print(max(target))
        return max(target, key=target.get)
        