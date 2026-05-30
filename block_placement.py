from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        N = 50001
        tree = [0] * (2 * N)

        def update(pos, val):
            pos += N
            tree[pos] = val
            while pos > 1:
                pos //= 2
                tree[pos] = max(tree[2*pos], tree[2*pos+1])

        def query(l, r):
            res = 0
            l += N
            r += N + 1
            while l < r:
                if l & 1:
                    res = max(res, tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = max(res, tree[r])
                l //= 2
                r //= 2
            return res

        obstacles = SortedList([0])
        results = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx      = obstacles.bisect_left(x) - 1
                prev     = obstacles[idx]
                gap      = x - prev
                update(x, gap)
                
                idx_next = obstacles.bisect_left(x)
                if idx_next < len(obstacles):
                    next_obs = obstacles[idx_next]
                    update(next_obs, next_obs - x)
                
                obstacles.add(x)
            else:
                x, sz = q[1], q[2]
                
                max_gap = query(0, x)
                
                idx  = obstacles.bisect_right(x) - 1
                prev = obstacles[idx]
                max_gap = max(max_gap, x - prev)
                
                results.append(sz <= max_gap)
        
        return results
