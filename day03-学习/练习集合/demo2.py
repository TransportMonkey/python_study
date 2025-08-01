class MyClass:
    class_variable = "I am a class variable"
    @classmethod
    def class_method(cls, arg1, arg2):
        print(f"Called with cls={cls}")
        print(f"Args: {arg1}, {arg2}")
        print(f"Access class variable: {cls.class_variable}")

    def test(self):
        self.class_method('32','44')
        self.is_palindrome(self, 'dsdd')
        print(f"Access class variable: {self.class_variable}")

    @staticmethod
    def is_palindrome(self, s):
        s = str(s).strip().lower()
        self.class_variable = 1
        print(s == s[::-1])


MyClass.class_method(12,44)
my_class = MyClass()
my_class.test()