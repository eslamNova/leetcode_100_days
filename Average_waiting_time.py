class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        w = 0
        
        t = customers[0][0]

        for c in customers:
            if t >= c[0]:
                t += c[1]
            else:
                t = c[0] + c[1]
            w += t - c[0]


        return w / len(customers)