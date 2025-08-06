from sqlalchemy import Column, Integer, String
from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm.session import sessionmaker

# 创建数据库（SQLite）
engine = create_engine("sqlite:///employee_system.db", echo=False)  # echo=False不查看SQL语句
# 创建基类
Base = declarative_base()

"""
一对多：一个部门可以有多个员工，一个员工只属于一个部门
"""


# 定义部门模型
class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    # 一对多关系：一个部门有多个员工
    employees = relationship(
        "Employee",
        back_populates="department",
        primaryjoin='Department.id==foreign(Employee.department_id)',
        uselist=True,

    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "employees": [emp.to_dict() for emp in self.employees]
        }

# 创建员工模型
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    department_id = Column(Integer, nullable=False)
    # 多对一的关系：员工属于一个部门
    department = relationship(
        "Department",
        back_populates="employees",
        primaryjoin='Department.id==foreign(Employee.department_id)',
        uselist=False,
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "department_id": self.department_id
        }

# 创建表
Base.metadata.create_all(engine)
# 创建会话
Session = sessionmaker(bind=engine)

class SessionClose:
    def __init__(self):
        self.session = Session()
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.session.commit()
        except:
            self.session.rollback()
        finally:
            self.session.close()

# 创建部门
def create_department(dept_name:str):
    with SessionClose() as session:
        dept = session.session.query(Department).filter_by(name=dept_name).first()
        if not dept:
            department = Department(name=dept_name)
            session.session.add(department)
            print(f'---> {dept_name}部门创建成功！')

        else:
            print('---> 该部门已存在！')


# 创建员工
def create_employee(emp_name: str, emp_email: str, department_id:int):
    with SessionClose() as session:
        empl = session.session.query(Employee).filter_by(name=emp_name).first()
        dept = session.session.query(Department).filter_by(id=department_id).first()
        if not dept:
            print('---> 该部门不存在！')
            return
        if not empl:
            # department = Department(name=department_name)
            employee = Employee(name=emp_name, email=emp_email, department=dept)
            session.session.add(employee)
            print(f'---> 员工：{emp_name} 创建成功！')

        else:
            print('---> 该员工已存在！')

# 1. 创建部门
dept_it = Department(name="IT部")
# with SessionClose() as sessions:
#     sessions.session.add(dept_it)
#     sessions.session.commit()
# dept_hr = Department(name="人力资源部")
# session.add(dept_it)
# session.add(dept_hr)
# session.commit()
# print("部门创建成功！")
# 先创建部门（如果尚未创建）
# dept_hr = session.query(Department).filter_by(name="人力资源部").first()
# if not dept_hr:
#     dept_it = Department(name="人力资源部")
#     session.add(dept_it)
#     session.commit()
#     print("部门创建成功！")

# 2. 创建员工
# emp1 = Employee(name="小五", email="sdsadsdg@qq.com",department=dept_it)
# emp2 = Employee(name="李四", email="lisi@example.com",department=dept_it)
# emp3 = Employee(name="王五", email="wangwu@example.com",department=dept_hr)
# session.add(emp1)
# session.add(emp2)
# session.add(emp3)
# session.commit()
# print("员工创建成功！")

create_employee('小花','dfsdffdg@qq.com',1)
# dept_hr = session.query(Department).filter_by(name="人力资源部").first()
# if dept_hr:
#     print(f'{dept_hr.name}: {dept_hr.employees[0].name}')
# # for user in users:
# #     print(f'{user.name}: {[todo.name for todo in user.todos]}')