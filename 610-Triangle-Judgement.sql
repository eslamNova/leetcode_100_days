# Write your MySQL query statement below

Select *, IF (x+y > z and y+z > x and z+x > y, "Yes", "No") as triangle From Triangle