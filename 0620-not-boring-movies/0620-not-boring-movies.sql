# Write your MySQL query statement below

select *from cinema where Not description = "boring" and mod(id, 2) = 1 order by rating DESC;
