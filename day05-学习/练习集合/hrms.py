"""
二、Python + SQLite3 实现更新与删除（所有功能均用代码实现）
员工管理系统
1、创建 employees 表：id, name, salary, department
2、实现：
update_salary(employee_id, new_salary) # 更新员工薪资
delete_employee(employee_id)  # 删除员工
query_low_salary_employees() # 查询薪资低于平均薪资的员工
"""
import sqlite3

class DBSwitch:
    def __enter__(self):
        self.conn = sqlite3.connect('my_test.db')
        self.cursor = self.conn.cursor()
        self.init_tb_employees()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

    # 创建employees表
    def init_tb_employees(self):
        tb_sql = '''
                 create table if not exists employee \
                 ( \
                     id         varchar(100) primary key, \
                     salary     double(10, 2), \
                     name       varchar(100) not null, \
                     department varchar(100) not null
                 );
                 '''
        self.cursor.execute(tb_sql)

# class DB(ABC):
#     def __init__(self):
#         self.conn = sqlite3.connect('my_test.db')
#         self.cursor = self.conn.cursor()
#         self.init_tb_employees()
#
#     # 创建employees表
#     def init_tb_employees(self):
#         tb_sql = '''
#                  create table if not exists employee \
#                  ( \
#                      id         varchar(100) primary key, \
#                      salary     double(10,2), \
#                     name       varchar(100) not null, \
#                       department varchar(100) not null
#                  );
#                  '''
#         self.cursor.execute(tb_sql)
#
#     @abstractmethod
#     # 关闭数据库连接
#     def close_db(self):
#         pass


class StaffingSystem:
    def __init__(self, db):
        self.cursor = db.cursor
        self.conn = db.conn

    # 插入员工数据
    def insert_employee(self, new_id:str, new_name:str, new_salary:float, new_department:str):
        insert_sql = f'insert into employee(id, name, salary, department) values ({new_id,}{new_name,}{new_salary,}{new_department})'
        self._execute_sql(insert_sql,need_resp=False)
        print(f'数据插入成功---> ')

    # 更新员工薪资
    def update_salary(self, employee_id:str, new_salary:float):
        upd_sql = f'update employee set salary={new_salary} where id={employee_id}'
        print(f'---> 更新{self._execute_sql(upd_sql)}员工薪资成功')

    # 删除员工
    def delete_employee(self, employee_id:str):
        del_sql = f"delete from employee where id='{employee_id}'"
        self._execute_sql(del_sql,need_resp=False)
        print(f'---> 删除成功!')
        # *args **kwargs
    # # 查询薪资低于平均薪资的员工
    def query_low_salary_employees(self):
        select_sql = 'select name from employee where salary <  (select avg(salary) from employee)'
        print(f'低于平均薪资的员工名单\n'
              f'----------{self._execute_sql(select_sql)}\n----------')

    # 查询
    def select_employee(self):
        select_sql = '''select * from employee'''
        print(self._execute_sql(select_sql,need_commit=False))

    # 执行并提交SQL语句
    def _execute_sql(self, sql,need_resp=True,need_commit=True):
        self.cursor.execute(sql)
        result =None
        if need_resp:
            result = self.cursor.fetchall()
        if need_commit:
            self.conn.commit()
        return result

with DBSwitch() as db:
    ss = StaffingSystem(db)
    # ss.select_employee()
    ss.insert_employee('005','小花',6797,'研发部')
