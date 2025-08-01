from abc import ABC, abstractmethod

class Animal(ABC):  # 抽象类
    @abstractmethod
    def speak(self):
        """子类必须实现这个方法"""
        pass

class Dog(Animal):
    def speak(self):
        return "汪汪！"

class Cat(Animal):
    def speak(self):
        return "喵喵~"

# 测试
dog = Dog()  # ✅ 成功，因为 Dog 实现了 speak
cat = Cat()  # ✅ 成功，因为 Cat 实现了 speak

# 如果有一个子类没实现 speak：
class Bird(Animal):
    pass

bird = Bird()  # ❌ 报错：TypeError: Can't instantiate abstract class Bird with abstract method speak