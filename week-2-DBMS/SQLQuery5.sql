use RevCompanyDb



select * from dept


select * from emp




select e.ename as 'Employee' , m.ename as 'Manager'
from emp e join emp m
on e.manager=m.empno

select *
from emp e cross join dept d

select * from dept

select ename
from emp
where deptno= (select deptno
from dept
where dname ='qc')

select ename from emp where sal> (select avg(sal) from emp)

select ename, deptno, sal from emp e
where sal<(select avg(sal) from emp where deptno=e.deptno);

select deptno, avgsal from (select deptno, avg(sal) as avgsal from emp group by deptno) as Details;
