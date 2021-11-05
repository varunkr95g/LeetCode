select distinct cnt67.Salary from
     ( select Salary,dense_rank() over(order by Salary desc) as rn 
     from Employee )
    cnt67 where cnt67.rn=N
