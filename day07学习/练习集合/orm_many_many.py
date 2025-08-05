from sqlalchemy import create_engine, Column, Integer, String,Table,ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

# 创建数据库引擎
engine = create_engine('sqlite:///course.db', echo=False)
Base = declarative_base()
# 定义学生和课程的关联表
student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('student.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('course.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    # course_id = Column(String) # 作为外键
    courses = relationship(
        "Course",
        secondary=student_course,
        back_populates='students',
        # primaryjoin='Student.id==foreign(Course.student_id)',
        uselist=True,
    )

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    # student_id = Column(Integer) # 作为外键
    students = relationship(
        "Student",
        secondary=student_course,
        back_populates='courses',
        # primaryjoin='Student.id==foreign(Course.student_id)',
        uselist=True,
    )

# 添加学生
def add_student(student_name: str):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        print(f"---> 学生{student_name}已存在！")
    else:
        s = Student(name=student_name)
        session.add(s)
        session.commit()
        print(f"---> 创建学生: {student_name}")

#删除学生
def delete_student(student_id:int):
        student_to_delete = session.query(Student).filter_by(id=student_id).first()
        if student_to_delete:
            session.delete(student_to_delete)
            session.commit()
            print(f'---> 成功删除{student_to_delete.name}！')
        else:
            print('---> 删除失败！学生ID不存在')

# 学生选课
def student_select_course(student_id: int, course_id: int):
    # 查询学生
    student = session.query(Student).filter_by(id=student_id).first()
    # 查询课程
    course = session.query(Course).filter_by(id=course_id).first()
    # 检查学生和课程是否存在
    if student and course:
        # 判断学生是否已选修课程
        if course in student.courses:
            print(f'{student.name} ---> {course.name}已是选修课程！')
        else:
            # 将课程添加到学生的课程列表中
            student.courses.append(course)
            # 提交更改
            session.commit()
            print(f'{student.name} ---> 成功选修了{course.name}课程！')
    else:
        print('---> 选课失败！学生或课程不存在')

# 学生退课
def student_remove_course(student_id: int, course_id: int):
    # 查询学生
    student = session.query(Student).filter_by(id=student_id).first()
    # 查询课程
    course = session.query(Course).filter_by(id=course_id).first()
    # 检查学生和课程是否存在
    if student and course:
        # 判断学生是否已选修课程
        if course in student.courses:
            # 将课程从学生的课程列表中移除
            student.courses.remove(course)
            # 提交更改
            session.commit()
            print(f'{student.name} ---> 成功退选了{course.name}课程！')
        else:
            print('---> 退课失败！学生未选修该课程')
    else:
        print('---> 退课失败！学生或课程不存在')

# 查询某学生的所有课程
def select_all_courses(student_id: int):
    all_courses = session.query(Student).filter(Student.courses.any(id=student_id)).all()
    # print(all_courses)
    students = session.query(Student).filter_by(id=student_id).all()
    if students:
        for student in students:
            all_coursess = [course.name for course in student.courses]
            if len(all_coursess) > 0:
                print(f'{student.name} ---> 所有选修的课程：{all_coursess}')
            else:
                print(f'{student.name} ---> 未选修任何课程！')
    else:
        print('---> 查询失败！学生不存在！')


# 课程中新增学生
def add_student_to_course(course_id:int, student_id:int):
        student = session.query(Student).filter_by(id=student_id).first()
        # 查询课程
        """
        """
        course = session.query(Course).filter_by(id=course_id).first()
        if student and course:
            # 判断课程中是否有该学生
            if student in course.students:
                print(f'{student.name} ---> 已存在于{course.name}课程中')
            else:
                course.students.append(student)
                session.commit()
                print(f'{student.name} ---> 成功添加到{course.name}课程中')
        else:
            print('---> 添加失败！学生或课程不存在')

# 添加课程
def add_course(course_name: str):
    course = session.query(Course).filter_by(name=course_name).first()
    if course:
        print(f"---> {course_name}课程已存在！")
    else:
        c = Course(name=course_name)
        session.add(c)
        session.commit()
        print(f"---> 创建课程: {course_name}")
    # all_courses = session.query(Course).all()
    # if course_name not in [course.name for course in all_courses]:
    #     session.add()
    #     session.commit()
    #     print(f'---> 新增课程：{course_name}')
    # else:
    #     print(f'---> {course_name}课程已存在，请换个课程！')

# 删除课程
def delete_course(course_id:int):
    course_to_delete = session.query(Course).filter_by(id=course_id).first()
    if course_to_delete:
        session.delete(course_to_delete)
        session.commit()
        print(f'---> 成功删除{course_to_delete.name}课程！')
    else:
        print('---> 删除失败！课程不存在')


# 课程中新增学生
def add_student_to_course(course_id:int, student_id:int):
    student = session.query(Student).filter_by(id=student_id).first()
    # 查询课程
    """
    """
    course = session.query(Course).filter_by(id=course_id).first()
    if student and course:
        # 判断课程中是否有该学生
        if student in course.students:
            print(f'{student.name} ---> 已存在于{course.name}课程中')
        else:
            course.students.append(student)
            session.commit()
            print(f'{student.name} ---> 成功添加到{course.name}课程中')
    else:
        print('---> 添加失败！学生或课程不存在')


# 课程中删除学生
def delete_student_to_course(course_id:int, student_id:int):
    student = session.query(Student).filter_by(id=student_id).first()
    # 查询课程
    course = session.query(Course).filter_by(id=course_id).first()
    if student and course:
        # 判断课程中是否有该学生
        if student in course.students:
            # course.students.remove(student)
            course.students.remove(student)
            session.commit()
            print(f'{student.name} ---> 已成功从{course.name}课程移除！')
        else:
            print(f'{student.name} ---> 移除失败！学生未选修该课程！')
    else:
        print('---> 删除失败！学生或课程不存在')


# 查询某课程的所有学生
def courses_all_student(courses_id:int):
    course = session.query(Course).filter_by(id=courses_id).first()
    if course:
        all_students = [student.name for student in course.students]
        if len(all_students) > 0:
            print(f'{course.name} ---> 被选修的学生：{all_students}')
        else:
            print(f'{course.name} ---> 未有学生选修！')
    else:
        print('---> 查询失败！课程不存在！')

# 查询没有被任何学生选修的课程
def not_selected_coursess():
    not_selectde_course = []
    courses = session.query(Course).filter(Course.students.any()).all()
    for course in courses:
        not_selectde_course.append(course.name)
    print(f"---> 没人选修的课程：{not_selectde_course}")

# 创建表
Base.metadata.create_all(engine)
# # 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# student = Student()
# add_student('小张') # 新增学生
# delete_student(3) # 删除学生
# student_select_course(2,1) # 学生选课程
# student_remove_course(2,1) # 学生退课程

# course = Course()
# add_course('化学') # 新增课程
# delete_course(9) # 删除课程
# add_student_to_course(1,2) # 从课程中添加学生
# delete_student_to_course(2,1) # 从课程中移除学生
# courses_all_student(5) # 查询某个课程所有学生
# not_selected_coursess() # 查询未被选修的课程
# session.close()
