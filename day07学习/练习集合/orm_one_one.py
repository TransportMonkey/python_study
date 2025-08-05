from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from typing import Dict

# 创建数据库引擎
engine = create_engine('sqlite:///products.db', echo=False)
Base = declarative_base()
# 手动创建表
# Base.metadata.create_all(engine)
# # 创建会话
Session = sessionmaker(bind=engine)
session = Session()

class BaseMy(Base):
    __abstract__ = True
    def to_dict(self,includes:list=None,excludes:list=None) -> Dict:
        if includes: # 按指定的字段名去获取数据
            return {k: v for k, v in self.__dict__.items() if not k.startswith('_') and k in includes}
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}


# 一对多关系
# 定义 users 模型
class User(BaseMy):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    # todo_id = Column(Integer)
    todos = relationship(
        'UserTodo',
        primaryjoin='User.id==foreign(UserTodo.user_id)',
        uselist=True,
    )

# 定义todo模型
class UserTodo(BaseMy):
    __tablename__ = 'user_todo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer) # 外键
    user = relationship(
        'User',
        primaryjoin='User.id==foreign(UserTodo.user_id)',
        uselist=False,
    )

users = session.query(User).all()
for user in users:
    print(f'{user.name}: {[todo.name for todo in user.todos]}')
