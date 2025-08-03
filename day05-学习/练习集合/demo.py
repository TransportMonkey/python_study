from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

from typing import List, Dict

# 创建数据库引擎
engine = create_engine('sqlite:///products.db', echo=False)
Base = declarative_base()

# Base.metadata.create_all(engine)
# # 创建会话
Session = sessionmaker(bind=engine)
session = Session()

class Basemy(Base):
    __abstract__ = True

    def to_dict(self,includes:list=None,excludes:list=None) -> Dict:
        if includes:
            return {k: v for k, v in self.__dict__.items() if not k.startswith('_') and k in includes}

        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

# 定义 Product 模型
class Product(Basemy):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    author_id = Column(Integer)

    # author = relationship(
    #     'Author',
    #     primaryjoin='Product.author_id==foreign(Author.id)',
    #     uselist=False,
    # )
    # aaa = Column(Float, nullable=True)
#
# class Author(Basemy):
#     __tablename__ = 'author'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String, nullable=False)
#
#     products = relationship(
#         'Product',
#         primaryjoin='Product.author_id==foreign(Author.id)',
#         uselist=True,
#     )

# 定义 users 模型
class User(Basemy):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    # todo_id = Column(Integer)
    todos = relationship(
        'UserTodo',
        primaryjoin='User.id==foreign(UserTodo.user_id)',
        uselist=True,
    )
#     # aaa = Column(Float, nullable=True)

class UserTodo(Basemy):
    __tablename__ = 'user_todo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer)
    user = relationship(
        'User',
        primaryjoin='User.id==foreign(UserTodo.user_id)',
        uselist=False,
    )
# # 创建会话
# Session = sessionmaker(bind=engine)
# session = Session()


# 定义 users 模型
class User(Basemy):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    # todo_id = Column(Integer)
    accounts = relationship(
        'UserAccount',
        primaryjoin='User.id==foreign(UserAccount.user_id)',
        uselist=True,
    )
    # aaa = Column(Float, nullable=True)

class UserAccount(Basemy):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    account_number = Column(String, nullable=False)
    user_id = Column(Integer)
    user = relationship(
        'User',
        primaryjoin='User.id==foreign(UserAccount.user_id)',
        uselist=False,
    )
# Base.metadata.create_all(engine)
# # 创建会话
# Session = sessionmaker(bind=engine)
# session = Session()
# u_1 = UserAccount(account_number='123', user_id=1)
# u_2 = UserAccount(account_number='123', user_id=1)
# session.add_all([u_1, u_2])
# session.commit()

# users = session.query(User).all()
# for user in users:
#     print(user.name,[account.account_number for account in user.accounts])

# todo_1 = UserTodo(name='睡觉',user_id=1)
# todo_2 = UserTodo(name='吃饭',user_id=1)
# # session.add(todo_1)
# # session.add(todo_2)
# session.add_all([todo_1, todo_2])
# session.commit()
# users = session.query(User).all()
# for user in users:
#     print(user.name,[todo.name for todo in user.todos])
# 创建表
# Base.metadata.create_all(engine)
# # a = Author()
# authors = session.query(Author).all()
# for author in authors:
#     product_names = [product.name for product in author.products]
#     print(author.name, "product:",product_names)
# print(authors[0])
# p = Product(name="czs",price=100,stock=100,author_id=1)
# session.add(p)

# print(p)
# 创建商品
def create_product(name: str, price: float, stock: int) -> Dict:
    new_product = Product(name=name, price=price, stock=stock)
    session.add(new_product)
    session.commit()
    return new_product.to_dict()
    # return {"id": new_product.id, "name": name, "price": price, "stock": stock}
#
# 查看某个商品
def get_product(product_id: int) -> Dict:
    # 查询指定id的商品
    product = session.query(Product).filter_by(id=product_id).first() # 返回Product类
    if product:
        return product.to_dict(includes=['id', 'name'],excludes=['id'])
        # return {"id": product.id, "name": product.name, "price": product.price, "stock": product.stock}
    return {}



if __name__ == '__main__':
    # create_product('被子',100,200)
    # 查看商品
    print(get_product(2))
    pass