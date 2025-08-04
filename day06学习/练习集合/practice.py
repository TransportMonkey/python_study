# 10、python内建数据类型有哪些？
"""str list dict tuple等"""
# 11、简述面向对象中__new__和__init__区别
"""__new__先调用，再到__init__调用"""
# 12、简述with方法打开处理文件帮我我们做了什么？
"""自动打开和自动关闭文件操作"""
# 13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
"""
def test(num):
    return num**2
list_ = [1,2,3,4,5]
res = map(test, list_)
print([n for n in list(res) if n > 10])
"""
# 14、python中生成随机整数、随机小数、0--1之间小数方法
"""
random.random()
"""
# 15、避免转义给字符串加哪个字母表示原始字符串？
"""r"""
# 16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
"""
str_ = <div class="nam">中国</div>
re.find(r'<div class=".*?">(.*?)</div>',str_)
"""

# 17、python中断言方法举例
"""
def test(num):
    assert num > 10
resr = test(3)
print(resr)
"""
# 18、数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
"""
# select distinct name from student;
"""
# 19、10个Linux常用命令
"""clear mkdir rm cp ifconfig cd ls pwd vim sudo"""

# 20、python2和python3的区别，请列举5个？
"""python2: range()返回是列表
   python3：range()返回是迭代对象
"""

# 21、列出python中可变数据类型和不可变数据类型，并简述原理
"""
可变数据类型：list、dict
不可变数据类型：str、int、tuple
可变数据类型可以去修改值，不可变数据不能修改值
"""
# 22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
"""
print(sorted(set(s)))
"""
# 23、用lambda函数实现两个数相乘
"""
lambda a,b:a*b
"""
# 24、字典根据键从小到大排序
"""
dict_ = {'asds':23,'s':5654}
print(sorted(dict_.keys())))
"""
# 25、利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
"""
print(Counter('kjalfj'))
print(Counter('ldsjafl'))
print(Counter('hdsllfdhg'))
print(Counter('lahfbl'))
print(Counter('hl'))
print(Counter('ahlf'))
print(Counter('h'))
"""
# 26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出张三  深圳
"""
a = "not 404 found 张三 99 深圳"
res = re.sub(r'[a-zA-Z0-9]','',a)
print(res) # 张三  深圳
"""

# 27、filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
def test(num):
    return num%2==1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = filter(test,a)
print(list(res))
"""
# 28、列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[num for num in a if num%2==1]
"""
# 29、正则re.complie作用?
"""
用于正则表达式字符串编译成一个正则表达式对象，
这个对象可以被用来执行、搜索、替换等操作，从而提高效率。
"""
# 30、a = (1,),b=1,c=("1")分别是什么数据类型？
"""
a是元组类型，b是int类型，c是字符串类型
"""
# 31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
"""
[1,5,7,9] + [2,2,6,8] 
"""
# 32、用python删除文件和用linux命令删除文件方法
"""
python删除文件:os.remove()
linux命令删除文件: rm -f
"""
# 33、log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
"""
import datetime
now_time = datetime.datetime.now()
print(now_time)
"""
# 34、请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
"""
Matplotlib、Seaborm、Plotly、Pyecharts
"""
# 35、写一段自定义异常代码
"""raise ValueError('出现异常！')"""

# 36、正则表达式匹配中，（.*）和（.*?）匹配区别？
"""
(.*):表示贪婪模式，尽可能匹配数据多一些
(.*?):表示非贪婪模式，尽可能匹配数据少一些
"""
# 37、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
"""
print([n for n in num for num in [[1,2],[3,4],[5,6]]])
"""
# 38、x = "abc",y="def",z=['d','e','f'],分别求出x.join(y)和x.join(z)
"""
x="abc"
y="def"
z=['d','e','f']
print(x.join(y)) # 'abcdef'
print(x.join(z)) # 'abcdef'
"""

# 39、举例说明异常模块中try except else finally的相关意义
"""
不管代码有没有捕获到异常，代码一样接着往finally里面走
"""
# 40、python中交换两个数值
"""
a,b = b,a
"""
# 41、举例说明zip（）函数用法
"""
a = ['1','2','3']
b = ['4','5','6']
new_list = list(zip(a,b))
print(new_list) # [('1','4'), ('2','5'), ('3','6')]
zip()的用法是传入两个列表，返回的是列表类型；列表中的每个元素是元组类型，
存储着两个列表相对应下标的值
"""
# 42、a="张明 98分"，用re.sub，将98替换为100
"""
a="张明 98分"
res = re.sub(r'\d+','100',a)
print(res)
"""
# 43、写5条常用sql语句
"""
use 数据库;
create database 数据库;
show databases;
desc 表名;
drop table 表名;
"""

# 44、a="hello"和b="你好"编码成bytes类型
"""
a="hello"
b="你好"
a_bytes = a.encode('utf-8')
b_bytes = b.encode('utf-8')
"""

# 45、[1,2,3]+[4,5,6]的结果是多少？
"""
[1,2,3,4,5,6]
"""
# 46、简述mysql和redis区别
"""
mysql是一种关系型数据库管理系统，使用SQL(结构化查询语言)进行数据操作；
redis是一种键值存储的非关系数据库，数据以键值对的形式存储
"""
# 47、正则匹配，匹配日期2018-03-20
"""
str_ = '就hash你就开2018-03-20始的反击得分'
res = re.findall(r'\d{4}-\d{2}-\d{2}',str_)
print(res) ['2018-03-20']
"""
# 48、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
"""
list=[2,3,5,4,9,6]
print(sorted(list))
"""
# 49、写一个单列模式
"""
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
# 测试代码
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # 输出：True
"""
# 50、保留两位小数
"""
a = 5
print(f'{a}:.2f')
"""
# 51、求三个方法打印结果
"""
a = '你好！中国'
print(a)
print(f'{a}')
print('{0}'.format(a))
"""
# 52、列出常见的状态码和意义
"""
200 正常访问网站
403 拒绝访问网站
404 请求资源不存在
500 网站服务器出错
503 服务器暂时无法处理请求，服务器可能过载或维护
"""
# 53、使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
"""
del dic['name']
dic.pop('name')
"""
# 54、列出常见MYSQL数据存储引擎
"""
InnoDB、MyISAM、Memory、Archive等
"""
# 55、计算代码运行结果，zip函数历史文章已经说了，得出[("a",1),("b",2)，("c",3),("d",4),("e",5)]
"""
list_1 = ['a','b','c','d','e']
list_2 = [1,2,3,4,5]
print(list(zip(list_1,list_2)))
"""