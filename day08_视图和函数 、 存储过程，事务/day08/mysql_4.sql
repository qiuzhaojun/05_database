查询综合练习:
1. 查询每位老师教授的课程数量
select teacher.tname,count(teacher_id)
from teacher left join course
on teacher.tid=course.teacher_id
group by tname;

2. 查询学生的信息及学生所在班级信息
select caption,sname,gender
from student left join class
on class.cid = student.class_id;

3. 查询各科成绩最高和最低的分数,形式 : 课程ID 课程名 最高分  最低分
select cid as 课程ID,cname as 课程名,max(number) as 最高分,min(number) as 最低分
from course left join score
on course.cid = score.course_id
group by cid,cname;

4. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select s.sid,sname,avg(number)
from student as s left join score
on s.sid = score.student_id
group by s.sid,sname
having avg(number) > 85;

5. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
select s.sid,s.sname,number
from student as s left join score
on s.sid = score.student_id
where course_id=2 and number > 80;

6. 查询各个课程及相应的选修人数
select cid,cname,count(*)
from course left join score
on course.cid = score.course_id
group by cid,cname;




将book表拆分为三个数据表 分别存储
图书信息  作家信息   出版社信息

自行设定三则的属性和关系
画出E-R图 然后根据图创建数据表

create table 作家 (
id int primary key auto_increment,
name varchar(30),
sex char,
remark text
);

create table 出版社(
id int primary key auto_increment,
pname varchar(30),
address varchar(256),
tel char(16)
);

create table 图书(
id int primary key auto_increment,
bname varchar(30),
price float,
aid int comment "关联作家表",
pid int comment "关联出版社表",
foreign key (aid) references 作家(id),
foreign key (pid) references 出版社(id)
);

create table author_press(
id int primary key auto_increment,
a_id int comment "关联作家表",
p_id int comment "关联出版社表",
foreign key (a_id) references 作家(id),
foreign key (p_id) references 出版社(id)
);

函数和存储过程

delimiter $$

create function st1() returns int
begin
update cls set score=99 where id=1;
delete from cls where score < 60;
return (select score from cls order by score desc limit 1);
end $$

delimiter ;


通过变量获取查询结果

create function st2() returns int
begin
declare a int;
declare b int;
set a=(select score from cls order by score desc limit 1);
select score from cls order by score limit 1 into b;
return a-b;
end

create function queryNameById(uid int)
returns varchar(20)
begin
return  (select name from cls where id=uid);
end $$

存储过程
create procedure st()
begin
    select name,age from cls;
    delete from cls where score < 60;
    select name,score from cls order by score desc;
end $$


存储过程变量测试

set @a=100;

create procedure p_in ( IN num int )
begin
    select num;
    set num=100;
    select num;
end $$

create procedure p_out ( OUT num int )
begin
    select num;
    set num=100;
    select num;
end $$

create procedure p_inout ( INOUT num int )
begin
    select num;
    set num=10000;
    select num;
end $$


练习:
1. 编写一个函数,传入两个同学的ID值,返回两位同学
的分数之差
create function fun(id_1 int,id_2 int)
returns float
begin
declare score_1 float;
declare score_2 float;
select score from cls where id=id_1 into score_1;
select score from cls where id=id_2 into score_2;
return score_1-score_2;
end $$


2. 编写一个存储过程, 通过用户变量传入学生的姓名
,使用该用户变量得到这个学生的成绩
create procedure get_score(inout stu varchar(30))
begin
set stu=(select score from cls where name=stu);
end $$

set @name="Lily";
call get_score(@name);
select @name;


