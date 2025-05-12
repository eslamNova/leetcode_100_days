class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        # k = []
        # h = defaultdict(list)
        # ans = 0 

        # for p in dominoes:
        #     k.append(sum(p))
        # print(k)


        # for i,p in enumerate(dominoes):
        #     h[k[i]].append(p)
        # print(h)

        # for p in h:
        #     no = False
        #     if len(h[p]) >= 2:
        #         a = h[p][0][0] 
        #         for j in h[p]:
        #             if a not in j:
        #                 no = True
        #                 break
        #         if not no:
        #             l = len(h[p])
        #             if l > 2:
        #                 ans += (l * (l-1)) // 2
        #             else:
        #                 ans += 1
        
        # return ans

        count = defaultdict(int)
        ans = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))  # normalize the domino
            count[key] += 1

        for v in count.values():
            if v > 1:
                ans += (v * (v - 1)) // 2  # combination C(n, 2)

        return ans
        
