use RevStudDb

begin transaction;

insert into dbo.student values (101,'AAA', 'QWERTY', 'BLR', 6524871);
insert into dbo.student values (102,'BBB', 'vbjhjiy','CHN', 6002586);

select *from student

save transaction level1;

insert into dbo.student (rollno, sname, pin)
values (103,'CCC', 6000259);

insert into dbo.student (sname, pin, rollno)
values ('DDD', 3456789, 104)

save transaction level2;

update student set addr='cgshidkni'
where rollno=103;

update student set city='HYD'
where rollno=103;

rollback transaction level2;

COMMIT TRANSACTION

update student set city='CHN'
where rollno=102;


delete from student where rollno=104;

truncate table student;

