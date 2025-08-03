from abc import ABC, abstractmethod
import sqlite3


class DB(ABC):
    def __init__(self):
        # 连接到数据库文件
        self.conn = sqlite3.connect('example.db')  # example.db ':memory:'内存数据库
        self.cur = self.conn.cursor()
    # def init_db(self):
    #     self.conn = sqlite3.connect('example.db')  # 连接到数据库文件 example.db ':memory:'内存数据库
    #     self.cur = self.conn.cursor()
    @abstractmethod
    def close_db(self):
        pass



class HandleAffairs(DB):
    def __init__(self):
        super().__init__()
        self.create_table()

    def create_table(self):
        table_sql = '''
                    create table if not exists test \
                    ( \
                        id     varchar(100) primary key, \
                        name   varchar(100)  not null, \
                        grades double(10, 1) not null
                    );
                    '''
        self.cur.execute(table_sql)

    # 插入数据
    def insert_action(self, id_:str, name_:str, grades:float):
        insert_sql = "insert into test(id,name,grades) values (?,?,?)"
        self.cur.execute(insert_sql, (id_,name_,grades))  # 插入多个数据
        self.conn.commit()
        print(f'insert ok ---> {(id_,name_,grades)}')
        self.close_db()

    # 更新数据
    def update_action(self, new_value:float, id_:str):
        update_sql = "update test set grades = ? where id = ?"
        self.cur.execute(update_sql, (new_value,id_))  # 插入多个数据
        self.conn.commit()
        print(f'update ok ---> {(new_value,id_)}')
        self.close_db()

    # 查询数据
    def select_action(self, id_):
        select_sql = "select * from test where id = ?"
        self.cur.execute(select_sql, (id_,))  # 插入多个数据
        self.conn.commit()
        result = self.cur.fetchall()
        print(f'select ok ---> {result}')
        for row in result:
            print(f'--------\n姓名：{row[1]}\n成绩：{row[2]}\n--------')
        self.close_db()

    # 删除数据
    def delete_action(self, id_):
        delete_sql = "delete from test where id = ?"
        self.cur.execute(delete_sql, (id_,))  # 插入多个数据
        self.conn.commit()
        print(f'delete ok ---> []')
        self.close_db()


    # 关闭游标&连接
    def close_db(self):
        self.cur.close()
        self.conn.close()


with HandleAffairs() as handle:
    pass
# handle.select_action('002') # 查询操作
# handle.update_action(57,'002') # 更新操作
# handle.insert_action('004','小石',78) # 插入操作
# handle.delete_action('002') # 删除操作