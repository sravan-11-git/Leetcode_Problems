# Write your MySQL query statement below


#select v.customer_id,count(v.customer_id) count_no_trans from visits v where v.visit_id not in (select visit_id #from transactions) group by v.customer_id;

select customer_id , count(visit_id) count_no_trans from visits  where visits.visit_id not in (select visit_id from transactions)  group by customer_id; 