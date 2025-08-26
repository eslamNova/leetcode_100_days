class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        mi = 0 
        md = 0
        for i in range(len(dimensions)):
            t = math.sqrt(dimensions[i][0]*dimensions[i][0] + dimensions[i][1]*dimensions[i][1]) 
            area = dimensions[i][0] * dimensions[i][1]
            if t > md or (t == md and area > ma):
                md = t
                ma = area
                mi = i
        
        return dimensions[mi][0] * dimensions[mi][1]
        