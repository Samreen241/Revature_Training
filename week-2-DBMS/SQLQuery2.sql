create database RevatureDB
use RevatureDB

CREATE TABLE details(
roll_no int,
sname varchar(50),
addr char,
city char,
pincode int
);

select * from details
alter table details
insert into details values (100, 'samreen', 'sdfghj' , 'Chennai', 600028, 'AS');

create database RevCompanyDb
use RevCompanyDb
create table dept(deptno smallint, dname varchar(3) not null,
constraint pk_deptno primary key (deptno));

create table emp(
empno smallint, 
ename varchar(30) not null,
manager smallint,
comm numeric(7,2),
deptno smallint,
constraint pk_empno primary key (empno),
constraint fk_deptno foreign key(deptno)references dept(deptno));

ALTER TABLE emp add sal numeric (10,2);


insert into dept values(10,'IT');
insert into dept values(20,'HR');
insert into dept values(30,'MKT');
insert into dept values(40,'SAL');
insert into dept values(50,'OPS');

select * from dept

INSERT INTO emp (empno, ename, manager, sal, comm, deptno) VALUES
(1001, 'Alice', NULL, 60000.00, NULL, 10),  -- HR
(1002, 'Bob', 1001, 75000.00, NULL, 20),    -- IT
(1003, 'Charlie', 1002, 50000.00, 500.00, 30), -- Sales
(1004, 'Diana', 1003, 52000.00, 300.00, 30),   -- Sales
(1005, 'Ethan', 1002, 58000.00, NULL, 40),  -- Finance
(1006, 'Fiona', 1005, 62000.00, NULL, 50);  -- Marketing

select * from  emp
select empno as "Employee number" from emp;  -- for column wise selections

select empno, ename, manager, comm, deptno, sal from emp where empno=1001;
select empno, ename from emp where empno !=1004

select empno as "Employee no", ename as "Name" from emp where empno in( 1004,1005,1002)

select empno as "Employee no", ename as "Name" from emp where ename in ('alice', 'fiona')

select empno as "Employee no", ename as "Name" from emp where empno not in( 1004,1005,1002)

select empno as "Employee no", ename as "Name" , sal as salary from emp where sal between 50000 and 60000

select empno as "Employee number", ename as "Employee name" from emp where ename like '__a%'

select empno as "Employee number", ename as "Employee name" from emp where ename not like '%a%'

select empno as "Employee number", ename as "Employee name" from emp where ename like '%a%' and empno=1004

select empno as "Employee number", ename as "Employee name" , sal as "Salary" from emp where sal>50000 order by sal desc;

select empno as "Employee number", ename as "Employee name" , sal as "Salary" from emp order by sal asc;



--- aggregation ---
select 
count(empno) as "No.of employees",
sum(sal) as "Sum of salary",
avg(sal) as "average of salary",
min(sal) as "Minimum is",
max(sal) as "Maximum is" from emp

select deptno as "Department" , sum(sal) as "Total salary" from emp where sal>60000 group by deptno

select deptno as "Department" , sum(sal) as "Total salary" from emp  group by deptno having sum(sal)>60000


------- joins -------

select e.ename,d.dname from emp e join dept d on e.deptno= d.deptno;