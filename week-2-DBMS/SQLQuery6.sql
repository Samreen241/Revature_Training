select * from emp;

create view vemp as select empno, ename from emp where deptno in (10, 20, 30);

select * from vemp

insert into emp(empno, ename, deptno) values (1110,'XXX', 20)

insert into vemp values (1111,'YYY')

update vemp set empno=10000 where empno=1111

delete from vemp where empno=1111
drop view vemp

create nonclustered index ideptno on emp(deptno)
drop index emp.ideptno

create or alter procedure sp_empdata
     @empno int, @ename varchar(20), @deptno int --parameters
as
begin
     begin transaction
     insert into emp (empno, ename, deptno) values(@empno, @ename, @deptno)
     commit
     select * from emp
end


exec sp_empdata 1015, 'Samreen', 20


create or alter procedure sp_empdata
     @empno int, @ename varchar(20),@sal numeric(10,2) ,@deptno int --parameters
as
begin
     begin transaction
     insert into emp (empno, ename,sal, deptno) values(@empno, @ename,@sal, @deptno)
     update emp set comm=sal*0.1 where empno=@empno
     commit
     select * from emp
     return 1
end

declare @status int
exec @status=sp_empdata 1018,'Shah',20,100
print @status