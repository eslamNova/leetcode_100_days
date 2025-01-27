class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        # d = {}
        # ans = []
        # # prerequisites = sorted(prerequisites, key= x[0])
        # prerequisites_sorted = sorted(prerequisites, key=lambda x: x[0])
        # for p in prerequisites_sorted:
        #     f = False
        #     # prerequisites = [[1, 2], [2, 3]]
        #     if p[0] in d:
        #         f = True

        #     if p[1] not in d:
        #         d[p[1]] = [p[0]]

        #         if f:
        #             for k in d[p[0]]:
        #                 d[p[1]].append(k)
        #             # d[p[1]].append(d[p[0]])

                
        #         # print(d)
        #     else:
        #         d[p[1]].append(p[0])
        # # print(d)

        # for q in queries:

        #     if q[1] in d:
        #         # print(d[q[1]])
        #         if q[0] in d[q[1]]:
        #             ans.append(True)
        #         else:
        #             ans.append(False)
        #     else:
        #         ans.append(False)

        # return ans
        # Initialize a 2D list to track prerequisites
        is_prerequisite = [[False] * numCourses for _ in range(numCourses)]
        
        # Mark direct prerequisites
        for u, v in prerequisites:
            is_prerequisite[u][v] = True
        
        # Propagate indirect prerequisites
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    # If i is a prerequisite for k, and k is a prerequisite for j,
                    # then i is also a prerequisite for j
                    if is_prerequisite[i][k] and is_prerequisite[k][j]:
                        is_prerequisite[i][j] = True
        
        # Answer queries
        ans = []
        for u, v in queries:
            ans.append(is_prerequisite[u][v])
        return ans
        