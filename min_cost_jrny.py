import heapq
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)

        min_time = [float('inf')] * n
        ph = []
        heapq.heappush(ph, (passingFees[0], 0, 0))  # (cost so far, current city, time so far)

        while ph:
            p, c, t = heapq.heappop(ph)
            # print(p, c, t)

            if c == n - 1 and t <= maxTime:
                return p

            for u, v, wt in edges:
                if u == c or v == c:
                    nei = v if u == c else u

                    nt = t + wt
    
                    if nt <= maxTime:
    
                        nc = p + passingFees[nei]


                        if nt < min_time[nei]:
                            min_time[nei] = nt
                            heapq.heappush(ph, (nc, nei, nt))

        return -1
