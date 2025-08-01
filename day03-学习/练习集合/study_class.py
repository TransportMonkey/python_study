class People:
    def __init__(self, name, age, sex): # 类的初始化化(构造函数)
        print(f'调用__init__') # 在类的实例化时，就调用__init__
        self.name = name
        self.age = age
        self.sex = sex
    def personal_data(self):
        people_info = f'-------\n姓名：{self.name}\n年龄：{self.age}\n性别：{self.sex}\n-------'
        print(people_info) # 打印个人信息
# ple = People('小明',24,'男') # 使用people类创建对象，传入三个参数
# ple.personal_data() # 调用personal_data函数

# 继承
class Animal:
    def __init__(self, name):
        print('___调用父类init___')
        self.name = name # 父类给子类继承
        self.__name = name  # 父类不给子类继承

    def eat(self):  # __eat表示不给子类继承这个方法
        print(f'{self.name}在吃东西')


class Dog(Animal): # dog是子类,animal是父类
    def __init__(self):
        super().__init__('旺财') #
# dg = Dog()
# dg.eat()

# 多态
class Animal:
    def __init__(self, name):
        print('___调用父类init___')
        self.name = name # 父类给子类继承
        self.__name = name  # 父类不给子类继承

    def eat(self):  # __eat表示不给子类继承这个方法
        print(f'{self.name}在吃东西')

    def sound(self):
        pass

class Cat(Animal): # dog是子类,animal是父类
    def __init__(self):
        super().__init__('旺财') #

    def sound(self):
        print('喵喵喵')

class Tiger(Animal): # dog是子类,animal是父类
    def __init__(self):
        super().__init__('旺财') #

    def sound(self):
        print('嗷呜')
def makesound(animal): # 封装
    animal.sound()
cat = Cat()
tiger = Tiger()
makesound(cat)
makesound(tiger)



