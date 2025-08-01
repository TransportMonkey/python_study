"""
一、封装（Encapsulation）
题目1：银行账户类
需求：
创建 BankAccount 类，包含私有属性 _account_number 和 _balance
提供以下方法：
deposit(amount)：存款（需校验金额为正数）
withdraw(amount)：取款（需校验余额是否充足）
get_balance()：返回当前余额
使用 @property 控制 account_number 为只读属性
"""
import os


class BankAccount:
    def __init__(self, account_number:str, balance=1000):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    # 存款
    def deposit(self, amount:int):
        if isinstance(amount, int):
            if amount < 0:
                raise ValueError('无效金额')
            self._balance += amount
            print(f'您的存款金额为: {amount}元')
        else:
            print('仅支持存1元或1元以上的金额！')

    # 取款
    def withdraw(self, amount:int):
        if self._balance >= amount:
            self._balance -= amount
            print(f'您的取款金额为：{amount}元')
        else:
            print('当前余额不足，请重新输入！')

    # 查看账户余额
    def get_balance(self):
        return self._balance
acc = BankAccount('123456789')
# acc.deposit(-100) # 存款
# acc.withdraw(200) # 取款
# print(f"账户：{acc.account_number} 余额：{acc.get_balance()}")

"""
二、继承（Inheritance）
题目2：图形类继承体系
需求：
定义抽象基类 Shape，包含抽象方法 area() 和 perimeter()
创建子类：
Rectangle：通过 length 和 width 计算面积和周长
Circle：通过 radius 计算面积和周长（π取3.14）

矩形面积：长 X 宽    周长：2 * (长+宽)
圆面积：3.14 * 半径的平方    周长：2 * 3.14 * 半径
"""
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name *2

    # @name.setter
    # def name(self,_name):
    #     self._name = _name

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__('矩形')
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    # def perimeter(self):
    #     return  2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self,radius):
        super().__init__('圆')
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
# a = Rectangle(63,4)
# print(a.perimeter())
# print(a.name)
# a.name =2
# print(a.name)
# shapes = [Rectangle(63, 4), Circle(5)]
# for shape in shapes:
#     print(f"{shape.name}面积: {shape.area():.2f}, 周长: {shape.perimeter():.2f}")

"""
三、多态（Polymorphism）
题目3：动物叫声模拟器
需求：
定义基类 Animal，包含抽象方法 speak()
创建子类 Dog、Cat、Duck，分别实现不同的 speak() 方法
编写函数 animal_concert(animals: list[Animal])，统一调用所有动物的 speak()
"""
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__('旺柴')

    def speak(self):
        print(self.name, '汪汪汪~')

class Cat(Animal):
    def __init__(self):
        super().__init__('猫咪')

    def speak(self):
        print(self.name, '喵喵喵~')

class Duck(Animal):
    def __init__(self):
        super().__init__('鸭子')

    def speak(self):
        print(self.name, '嘎嘎嘎~')

def animal_concert(animal:list):
    for aml in animal:
        aml.speak()
# dog = Dog()
# cat = Cat()
# duck = Duck()
# animal_concert([dog,cat,duck])

# import Fraction
"""
四、特殊方法（Magic Methods）
题目4：自定义分数类
需求：
创建 Fraction 类，初始化时接受 numerator（分子）和 denominator（分母）
重写以下特殊方法：
__str__：返回分数形式（如 "3/4"）
__add__：实现分数加法（返回新的 Fraction 对象）
__eq__：判断两个分数是否相等
"""
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError('分母不能为0')
        # self.gcd_vlue = math.gcd(numerator, denominator) # math.gcd(a, b) 返回最大公约数
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("只能与 Fraction 相加")
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator / other.numerator == self.denominator / other.denominator

# f1 = Fraction(1, 2)
# f2 = Fraction(3, 4)
# print(f1 + f2)  # 输出: 10/8（不进一步约分，符合题目要求）
# print(Fraction(2, 4) == Fraction(1, 2))  # False

"""
五、类方法与静态方法
题目5：字符串工具类
需求：
创建 StringUtils 类，包含：
类方法 from_file(cls, filename)：读取文件内容返回字符串
静态方法 is_palindrome(s)：判断字符串是否为回文（正反序都是一样的内容，如 12321，1221）
"""
class StringUtils:
    # cls --> StringUtils
    @classmethod
    def from_file(cls, filename):
        res = cls.is_palindrome('dfdfdf')
        print(res)
        if not os.path.exists(filename):
            raise ValueError('文件不存在！')
        with open(filename, 'r',encoding='utf-8') as f:
            file_contents = f.read()
            return file_contents

    @staticmethod
    def is_palindrome(s):
        s = str(s).strip()
        return s == s[::-1]
# text = StringUtils.from_file("tmp_data.txt")
# print(text)  # 输出文件内容
# print(StringUtils.is_palindrome("racecar"))  # True

"""
六、综合应用
题目6：简易购物车系统
需求：
设计 Product 类（属性：id, name, price）
设计 ShoppingCart 类，包含方法：
add_product(product, quantity=1) 
remove_product(product_id)
get_total()：计算总价
使用字典存储商品及其数量
"""
class Product:
    """商品类"""
    def __init__(self, id_: int, name: str, price: float):
        self.id_ = id_
        self.name = name
        self.price = price

    # 1. 类对象(内存地址)      -->  实例的类   调用方法，调用属性  <class '__main__.Product'>
    # 2. __repr__  -->  字符串   str Product(id=21, name=苹果, price=32.4)
    # print(p1)、p1.__repr__、p1(obj)
    def __repr__(self):
        return f"str Product(id={self.id_}, name={self.name}, price={self.price})"

# p1 = Product(21,'苹果',32.4) # 实例化一个类，变量对象，方法对象，类对象
# p1 = Product(1, "苹果", 5.5)
# p2 = Product(2, "香蕉", 3.0)
# cart = ShoppingCart()
# cart.add_product(p1, 2)
# cart.add_product(p2)
# print(f"总价: {cart.get_total()}")  # 输出: 总价: 14.0


class ShoppingCart:
    """购物车类，用字典保存 {product 对象: 数量}"""
    def __init__(self):
        self._items = {}  # key: Product, value: int

    def add_product(self, product: Product, quantity: int = 1):
        """添加商品，默认数量为 1"""
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self._items[product] = self._items.get(product, 0) + quantity

    def remove_product(self, product: Product, quantity: int = 1):
        """按商品 id 移除（移除）"""
        # 对应商品在不在购物车中，也就是判断键在不在self._items
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if self._items.get(product) is None:
            print('商品不在购物车')
            return
        # 1、删除的商品数量大于或者等于购物车里的商品数量
        if quantity >= self._items.get(product):
            del(self._items[product])
            print('删除该商品')
            return
        # 2、删除的商品数量小于购物车里的商品数量
        self._items[product] -= quantity

    def get_total(self) -> float:
        """计算购物车总价"""
        price = 0
        for p, q in self._items.items(): # {Product('12','dsd',43):4,Product('12','dsd',43),6} Product.price
            price += p.price * q
        return price

    # 可选：方便调试
    def __repr__(self):
        return f"ShoppingCart({self._items})"
# apple  = Product(1, "苹果", 3.5)
# print(apple)
# banana = Product(2, "Banana", 2.0)
# cart = ShoppingCart()
# cart.add_product(apple, 3)      # 3 个苹果
# cart.add_product(banana, 5)      # 3 个苹果
# cart.remove_product(apple,4)          # 移除苹果
# print("总价:", cart.get_total())  # 3.5*3 + 2.0*1 = 12.5
# cart.add_product(banana)        # 1 根香蕉
# cart.add_product(apple, 2)      # 2 个苹果
# print("总价:", cart.get_total())  # 2.0


"""
题目7：上下文管理器实现计时器
需求：
创建 Timer 类，实现 __enter__ 和 __exit__
进入时记录开始时间，退出时打印执行耗时
"""
import time
class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter() - self.start_time
        print(f'代码块执行耗时: {self.end_time:.2f}s')
# with Timer():
#     sum(range(100000000))


# 实现单例模式
class Singleton:
    _instance = None # 类的属性
    def __new__(cls, *args, **kwargs): #
        print(Singleton._instance)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = all([Singleton() for i in range(100)])
print(s1)  # True







