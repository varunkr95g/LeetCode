select tot.Request_at as Day, ROUND(COALESCE((can.total_canc/tot.total_trp),0.00),2) as "Cancellation Rate"
from
( select count(*) as total_trp, trp.Request_at from Trips trp
left outer join Users usr1
on usr1.Users_Id=trp.Client_Id
left outer join Users usr2
on usr2.Users_Id=trp.Driver_Id
where usr1.Banned='No'
and usr2.Banned='No'
group by trp.Request_at
) tot
left outer join
(
select count(*) as total_canc, trp.Request_at from Trips trp
left outer join Users usr1
on usr1.Users_Id=trp.Client_Id
left outer join Users usr2
on usr2.Users_Id=trp.Driver_Id
where usr1.Banned='No'
and usr2.Banned='No'
and trp.Status in('cancelled_by_driver','cancelled_by_client')
group by trp.Request_at
) can
on tot.Request_at=can.Request_at
where tot.Request_at in ("2013-10-01","2013-10-02","2013-10-03")
