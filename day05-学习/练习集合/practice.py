# use test_db;
# # 一：学生选课系统表设计
# # 需求（写出对应sql）：
# # 1、创建以下表结构：
# # students（学生表）：id（主键）, name, age
# create table if not exists students(
#         id varchar(100) primary key,
#         name varchar(100) ,
#         age int
# );
# # courses（课程表）：id（主键）, name, teacher
# create table if not exists courses(
#         id varchar(100) primary key,
#         name varchar(100),
#         teacher varchar(100)
# );
# # student_course（选课表）：student_id（外键）, course_id（外键）
# create table if not exists student_course(
#         student_id varchar(100),
#         course_id varchar(100),
#         foreign key (student_id) references students(id),
#         foreign key (course_id) references courses(id)
# );
# # 2、编写SQL语句完成以下操作：
# # 查询年龄大于20的学生姓名
# select name from students where age > 20;
#
# # 查询被选修次数最多的课程名
# select c.name from courses c inner join student_course sc
# on c.id = sc.course_id group by c.id order by
# count(sc.student_id) desc limit 1;
#
# # 查询没有选课的学生名单
# select s.name from students s inner join student_course sc
# on s.id = sc.student_id where sc.student_id is null;
#
# # 更新：将学生 "Alice" 的年龄改为 22 岁
# update students set age = 22 where name = 'Alice';
#
# # 删除：删除所有未被任何学生选修的课程
# delete from courses where id not in(select distinct course_id from student_course);
#
# # 级联删除：删除学生 "Bob" 及其所有选课记录
# delete from students where name = 'Bob';