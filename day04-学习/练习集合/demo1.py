import copy
 # 引用
a = 'hello' # 0x234
b = a # 0x234
# print(f'a:{hex(id(a))}')
# print(f'b:{hex(id(b))}')
# a = '32323' # 0x234
# print(f'b:{hex(id(b))}')
# print(f'a:{a}') # 'hello'
# a = 'haha'
# print(f'b:{b}') # 'hello'
# c = ['1','3','4']
# d = c # ['1','3','4']
# print(d) # ['1','3','4']
# c = ['a','b','c']
# c[2] = {'abc':123} # ['1','3',{'abc':123}]
# print(c) # ['a','b',{'abc':123}]
# print(d) # ['1','3','4']

# 浅拷贝
a = [['a','b'],2,3,4,["1","2"]]  #["1","2"] x1234


print(f'a:{a}') # [1,2,3,4]
b = copy.copy(a) # [1,2,3,4,["1","2"]]  x1234

a [1] = 10
a[0][0]=100
print(f'a:{a}') # [['a',2],2,3,4,[6,"2"]]
print(f'b:{b}') # [['a',2],2,3,4,[6,"2"]]
#
# c = [1,['a','c'],4]
# print(f'c:{c}') # [1,['a','c'],4]
# d = copy.copy(c)
# c[1][1] = 'g'
# # c[2]['abc'] = 'haha'
# print(f'c:{c}') # [1,['a','g'],4]
# print(f'd:{d}') # [1,['a','g'],4]


# 深拷贝
e = [1,['a','c'],4]
print(f'e:{e}') # [1,['a','c'],4]
f = copy.deepcopy(e)
e[0] = 'hehe'
print(f'e:{e}') # ['hehe',['a','c'],4]
print(f'f:{f}') # [1,['a','c'],4]]


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance: # None
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance # obj


    def __init__(self, value): # self.
        self.value = value # 100



# 测试
# a = list(set(Singleton(200) for i in range(2)))
# print(hex(id(a[0])))

a = Singleton(100)
print(a.value)
# b = Singleton(200)
# print(b.value)
#
# print(a.value)



# a = 3
# b = a
# print(f'a: {a}  addr: {hex(id(a))}')
# print(f'b: {b}  addr: {hex(id(b))}')
# a1 = '456' # 0x678
# print(f'a: {a1}  addr: {hex(id(a1))}')
# print(f'a: {b}  addr: {hex(id(b))}')






























