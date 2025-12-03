create database RevCompanyDb

use RevCompanyDb

create table dept(deptno smallint, dname varchar(3)not null,
constraint pk_deptno primary key (deptno));


create table emp(empno smallint, ename varchar(30) not null,mgr smallint, sal numeric(10,2),comm numeric(7,2),
deptno smallint,constraint pk_empno primary key(empno),
constraint fk_deptno foreign key(deptno) references dept(deptno));

insert into dept values(80, 'IT')
insert into dept values(90, 'HR')
insert into dept values(45, 'SAL')
insert into dept values(60, 'MKT')
insert into dept values(70, 'OPS')

select * from dept

INSERT INTO emp (empno, ename, mgr, sal, comm, deptno) VALUES
(1001, 'Alice', NULL, 60000.00, NULL, 10), 
(1002, 'Bob', 1001, 75000.00, NULL, 20),   
(1003, 'Charlie', 1002, 50000.00, 500.00, 30),
(1004, 'Diana', 1003, 52000.00, 300.00, 30),   
(1005, 'Ethan', 1002, 58000.00, NULL, 40), 
(1006, 'Fiona', 1005, 62000.00, NULL, 50);

Select * from emp

select empno, ename from emp;

select empno as "Emp Num", ename as "Name" 
from emp
where sal>60000;

select empno as "Emp Num", ename as "Name" 
from emp
where empno !=1004


select empno as "Emp Num", ename as "Name" 
from emp
where empno not in (1002, 1003, 1005)

select empno as "Emp Num", ename as "Name" 
from emp
where sal between 40000 and 55000

select empno as "Emp Num", ename as "Name" 
from emp
where ename LIKE '_a%';

select empno as "Emp Num", ename as "Name" 
from emp
where ename not in ('alice', 'fiona');

select empno as "Emp Num", ename as "Name" 
from emp
where empno=1004 and ename LIKE '%a%';

select empno as "Emp Num", ename as "Name", sal as 'Salary' , comm as 'Commission'
from emp
order by comm asc,sal desc;

select count(empno) as 'No of Emp', sum(sal) as 'Total', avg(comm) as 'Avg Comm',min(sal) as 'Least Salary', max(sal) as 'Top earner'
from emp


select deptno as 'Department', sum(sal) as 'Total Salary'
from emp
group by deptno
having deptno in (10, 20, 30);

INSERT INTO emp (empno, ename, mgr, sal, comm, deptno) VALUES
(1007, 'AAA', NULL, 60000.00, NULL, NULL), 
(1008, 'BB', 1001, 75000.00, NULL, NULL),   
(1009, 'C', 1002, 50000.00, 500.00, NULL)

 select e.ename, d.dname
 from emp e  LEFT OUTER join dept d
 on d.deptno = e. deptno;
