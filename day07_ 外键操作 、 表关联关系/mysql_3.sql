--外键关联
insert into dept values (1,"技术部"),(2,"销售部"),(3,"市场部"),(4,"行政部"),(5,'财务部'),(6,'总裁办公室');


insert into person values
(1,"Lily",29,'w',20000,'2017-4-3',2),
(2,"Tom",27,'m',16000,'2019-10-3',1),
(3,"Joy",30,'m',28000,'2016-4-3',1),
(4,"Emma",24,'w',8000,'2019-5-8',4),
(5,"Abby",28,'w',17000,'2018-11-3',3),
(6,"Jame",32,'m',22000,'2017-4-7',3);

级联动作
alter table person add
foreign key(dept_id)
references dept(id)
on delete cascade on update cascade;

alter table person
add foreign key(dept_id)
references dept(id)
on delete set null on update set null;

--练习: 将微信用户朋友圈表进行重新设计
--根据所学的关系模型将其合理化

用户表
create table user(
id int primary key auto_increment,
name varchar(30) not null,
passwd char(64),
tel char(16)
);

朋友圈
create table pyq(
id int primary key auto_increment,
image blob,
content text,
time datetime,
u_id int comment "关系字段",
foreign key (u_id) references user(id)
);

点赞评论
create table like_talk(
id int primary key auto_increment,
uid int,
pid int,
`like` bit,
talk text,
foreign key (uid) references user(id),
foreign key (pid) references pyq(id)
);

查询综合练习:
1. 查询每位老师教授的课程数量
select teacher.tname,count(teacher_id)
from teacher left join course
on teacher.tid=course.teacher_id
group by tname;


2. 查询学生的信息及学生所在班级信息
3. 查询各科成绩最高和最低的分数,形式 : 课程ID  最高分  最低分
4. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
5. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
6. 查询各个课程及相应的选修人数




