create database student;
use student;
-- 创建数据表
 create table class_1 (
 id int primary key auto_increment,
 name varchar(30) not null,
 age tinyint unsigned,
 sex enum('m','w','o'),
 score float default 0
 );

 create table hobby (
 id int primary key auto_increment,
 name varchar(30) not null,
 hobby set("dance","sing","draw"),
 level char comment "初始评级",
 price decimal(7,2),
 remark text comment "备注信息"
 );


-- 插入class_1表数据
insert into class_1 values
(1,"Lily",18,'w',86),
(2,"Tom",17,'m',68),
(3,"Tonny",18,'m',91);

insert into class_1
(name,age,sex) values
("Joy",19,'m');

insert into class_1
(name,age,score) values
("Emma",17,93);

insert into class_1
(name,age,sex,score) values
("Alex",19,'m',77),
("Levi",18,'m',73),
("Sunny",19,'w',84);

-- 插入hobby表数据
insert into hobby
values
(1,"Joy","dance,sing","A",49800.00,"骨骼惊奇,练舞奇才"),
(2,"Jame","sing","B",9800.00,"天籁之音"),
(3,"Lily","draw","B",19800.00,"达芬奇再世");

insert into hobby
(name,hobby,level,price) values
("Emma","draw,sing",'C',36000.00),
("Lucy","dance",'B',8800.00),
("Baron","draw",'A',16000.00);







