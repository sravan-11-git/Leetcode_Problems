# Write your MySQL query statement below



select pro.product_name, sal.year, sal.price from sales sal,product pro where pro.product_id = sal.product_id;