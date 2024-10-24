#O(N2)
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # حساب إسقاط xy
        xy_projection = sum(1 for row in grid for val in row if val > 0)
        
        # حساب إسقاط yz (أكبر قيمة في كل صف)
        yz_projection = sum(max(row) for row in grid)
        
        # حساب إسقاط zx (أكبر قيمة في كل عمود)
        zx_projection = sum(max(col) for col in zip(*grid))
        
        # المساحة الإجمالية
        return xy_projection + yz_projection + zx_projection

        