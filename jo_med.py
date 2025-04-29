class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m_n, m_c = max(nums), 0
        l = 0
        ans = 0

        for r in range(len(nums)):
            if nums[r] == m_n:
                m_c += 1
            while m_c > k or (l <= r and m_c ==k and nums[l] != m_n):
                if nums[l] == m_n:
                    m_c -= 1
                l += 1
            if m_c ==k:
                ans += l+1
        return ans
        