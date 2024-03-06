# Write your MySQL query statement below

SELECT p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
FROM Prices p LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND
u.purchase_date BETWEEN start_date AND end_date
group by product_id



 
 
 
 /*select distinct table2.product_id , table2.nume,(table2.nume / table2.deno ) as average_price from 
 
(select table1.product_id , table1.price , table1.units , table1.deno,  table1.nume from 

(select pr.product_id , pr.price , un.units , sum(un.units) as deno, (pr.price * un.units) as nume from prices pr inner join unitssold un on un.product_id = pr.product_id group by pr.product_id) table1 ) as table2*/
 
 
 