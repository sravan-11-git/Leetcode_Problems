# Write your MySQL query statement below

select w2.id from weather w1 inner join weather w2 on w2.temperature > w1.temperature and datediff(w2.recordDate,w1.recordDate) = 1;









