from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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

# 定义 Product 模型
class Product(BaseMy):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    author_id = Column(Integer)

# 创建商品
def create_product(name: str, price: float, stock: int) -> Dict:
    new_product = Product(name=name, price=price, stock=stock)
    session.add(new_product)
    session.commit()
    return new_product.to_dict()

# 查看某个商品
def get_product(dest_product_id: int) -> Dict:
    product_data = {}
    # 查询指定id的商品
    product = session.query(Product).all() # 返回Product类
    for product in product:
        if product.id == dest_product_id:
            product_data =  product.to_dict(includes=['id','name'])
        else:
            product_data = {}
    return product_data

get_data = get_product(1)
print(get_data)