def a(var1:int):
    print(f'{a.__name__}:{id(a)}', var1**5)
def b(var2:int):
    print(f'{b.__name__}:{id(b)}', var2**4)

data = {'aa':a,'bb':b}
data['aa'](5)
data['aa'](2)
