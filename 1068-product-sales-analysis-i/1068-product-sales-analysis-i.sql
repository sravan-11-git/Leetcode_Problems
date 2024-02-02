# Write your MySQL query statement below

select pro.product_name ,sal.year,sal.price from sales sal join product pro on sal.product_id = pro.product_id;