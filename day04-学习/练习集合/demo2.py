# 1、一行代码实现1--100之和
sum(range(1,101))

# 2、如何在一个函数内部修改全局变量
g = 4
def test():
    global g
    g += 1
test()

# 3、列出5个python标准库
"""
os 、sys、random、string、re
"""

# 4、字典如何删除键和合并两个字典
a = {'a':'123','b':'456'}
b = {'abc':'ddd','net':'434'}
del a['b']
for key_,value in a.items():
    b[key_] = value

# 5、谈下python的GIL
"""
GIL锁主要是应用在线程中，线程在计算机运行是一起并行的，
为了让每个线程之间运行独立互不干扰，所以就要拿到GIL锁，
否则就会一直在等前面的线程GIL释放了，然后拿到锁后才能执行下一步操作。
"""

# 6、python实现列表去重的方法
set()

# 7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
"""
*args是把多个未使用的参数打包成一个元组类型
*kwargs是把多个未使用的参数打包成一个字典类型
"""

# 8、python2和python3的range（100）的区别
"""
python2的range(100)是返回列表类型
python3的range(100)是返回是迭代对象
"""

# 9、一句话解释什么样的语言能够用装饰器?
"""
装饰器是一个函数，可以接收函数名，也可以返回函数名的语言，都可以用装饰器
"""

# 10、python内建数据类型有哪些？
"""
元组、列表、字典、字符串、整型等。
"""
