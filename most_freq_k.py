# O(NLogN)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        ans = []
        for i in range(k):
            ans.append(c.most_common()[i][0])
            # print(ans)

        return ans
    