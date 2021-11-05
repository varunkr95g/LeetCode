select cnt67.Department,cnt67.Employee,cnt67.Salary from
(
select Emp.Name as Employee,Emp.Salary,Dept.Name as Department,dense_rank() 
over(partition by Emp.DepartmentId order by Salary desc ) as dr
from Employee Emp left outer join Department Dept
on Emp.DepartmentId=Dept.Id
) cnt67
where cnt67.dr=1
