select distinct X.Num as ConsecutiveNums from
(select Num,lead(Num) over(order by Id) as lead_1
,lead(Num,2) over(order by Id) as lead_2
from Logs
 ) X where (X.Num=X.lead_1) and (X.lead_1=X.lead_2) ;
