class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # c = []
        # for i in range(len(s)-2):
        #     for j in range(i+1,len(s)-1):
        #         for k in range(j+1,len(s)):
        #             st = s[i]+s[j]+s[k]
        #             if st == st[::-1]:
        #                 c.append(st)
                        
        # return len(set(c))
        letters = set(s)
        ans = 0
        
        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()
            
            for k in range(i + 1, j):
                between.add(s[k])
            
            ans += len(between)

        return ans
        