# dict()创建字典新方法
"""
res_1 = dict(name="小林",age=24)
print(res_1) # {'name':'小林','age':24}
"""
# 61、简述同源策略
"""
同源策略需要同时满足以下三点要求： 
1）协议相同 
2）域名相同 
3）端口相同 
 http:www.test.com与https:www.test.com 不同源——协议不同 
 http:www.test.com与http:www.admin.com 不同源——域名不同 
 http:www.test.com与http:www.test.com:8081 不同源——端口不同
 只要不满足其中任意一个要求，就不符合同源策略，就会出现“跨域”
"""
# 62、简述cookie和session的区别
"""
cookie是存在客户端，session是存在服务端；
session.id存在cookie中，如果浏览器禁用了cookie，同时session也会失效，
cookie安全性比seeion的差
"""
# 63、简述多线程、多进程
"""
多线程：多线程是指一个程序内部有多个线程同时运行。线程是程序执行的最小单位，也是进程的子单位，共享进程的资源（如内存空间）。
多进程：进程是指多个进程同时运行。每个进程是独立的程序，拥有自己的内存空间。
协程：协程是共用进程的内存空间，比线程更轻量（消耗系统资源更少）
"""
# 64、简述any()和all()方法
"""
any(): 接收是一个迭代对象，迭代对象里面的元素只要是一个为真，返回的是True
all(): 接收是一个迭代对象，迭代对象里面的元素所有元素都为真，返回的是True
"""
# 65、IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
"""
IOError: 输入输出异常
AttributeError：访问一个对象里面没有属性
ImportError：没有正确引入模块或包，基本是路径的问题
IndentationError：语法错误，代码没有正确对齐
IndexError：下标超过序列的边界
KeyError：访问字典里不存在的键
SyntaxError：代码语法错误
NameError：变量还未定义
"""
# 66、python中copy和deepcopy区别
"""
copy: 复制最外层的内存地址(除了int,str,tuple)
a = ['a','b','c']
print(a) # ['a','b','c']
b = copy.copy(a) # 浅拷贝
a[0] = 4
print(a) # [4,'b','c']
print(b) # ['a','b','c']

c= [[4,'r'],'d','345']
print(c) # [[4,'r'],'d','345']
d = copy.copy(c) # 浅拷贝
c[0][0] = '55'
print(c) # [[55,'r'],'d','345']
print(d) # [[55,'r'],'d','345']

deepcopy: 完全复制新的内存地址
f = ['a','b','c']
print(f) # ['a','b','c']
g = copy.deepcopy(f)
f[0] = [1,2,3]
print(f) # [[1,2,3],'b','c']
print(g) # ['a','b','c']
"""
# 67、列出几种魔法方法并简要介绍用途
"""
__init__:对象初始化方法
__new__:创建对象时候执行的方法，单列模式会用到
__str__:当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
__del__:删除对象执行的方法
"""
# 68、C:\Users\ry-wu.junya\Desktop>python 1.py 22 33命令行启动程序并传参，print(sys.argv)会输出什么数据？
"""
sys.argv是sys模块中的一个列表,第一个元素是脚本名称，
其它元素是命令行传参给脚本的参数
print(sys.argv) # ['1.py','22','33']
"""
# 69、请将[i for i in range(3)]改成生成器
"""
gen = (i for i in range(3)) # python3
"""
# 70、a = "  hehheh  ",去除收尾空格
"""
a = ' hehheh '
print(a.strip()) # 'hehheh'
"""
# 71、举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
"""
sort方法：
list_=[0,-1,3,-10,5,9]
list_.sort()
print(list_) # [-10,-1,0,3,5,9]

sorted方法
list_=[0,-1,3,-10,5,9]
print(sorted(list_)) # [-10,-1,0,3,5,9]
print(list_) # [0,-1,3,-10,5,9]
"""
# 72、对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
"""
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
new_foo = sorted(foo,key=lambda x:x)
print(new_foo) # [-20, -5, -4, -4, -2, 0, 2, 4, 8, 8, 9]
"""
# 73、使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
"""
# 正数从小到大，负数从大到小
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
new_foo = sorted(foo,key=lambda x:(x<0,abs(x))) # abs()取绝对值
print(new_foo) # [0, 2, 4, 8, 8, 9, -2, -4, -4, -5, -20]
# 正数从大到小，负数从小到大
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
new_foo = sorted(foo,reverse=True,key=lambda x:(x>0,abs(x)))
print(new_foo)
"""
# 74、列表嵌套字典的排序，分别根据年龄和姓名排序
"""
print(sorted(foo,key=lambda x:(x['name'],x['age'])))
"""
# 75、列表嵌套元组，分别按字母和数字排序
"""
list_ = [('sw',46),('s4gw',65),('r475',76)]
print(sorted(list_,key=lambda x:x[0]))
print(sorted(list_,key=lambda x:x[1]))

key: 返回可以是值，也可以是元组
"""
# 76、列表嵌套列表排序，年龄数字相同怎么办？
"""
a = [['sds',54],['gf44',433],['gfg56',433],['tfgr',433],['f343',54]]
print(sorted(a,key=lambda x:x[1]))
"""
# 77、根据键对字典排序（方法一，zip函数）
"""
dict_ = {'sad2':32,'dfvv3':433,'2ed33':86}
list_ = list(zip(dict_.keys(),dict_.values()))
tuple_ = [i for i in list_]
item_ = sorted(tuple_,key=lambda x:x[0])
# print(key_)
new_dict = {d[0]:d[1] for d in item_}
print(new_dict)
"""
# 78、根据键对字典排序（方法二,不用zip)
"""
字典是有序的
# 按键对字典排序（不用zip方法）
b = {'name':'dsdd','dsw332':434,'dsc34':65,'323dd':4367}
key_sort = sorted(b.items(), key=lambda x:x[0])
new_dict = { d[0]:d[1] for d in key_sort}
print(new_dict)
"""
# 79、列表推导式、字典推导式、生成器
"""
list_ = [i for i in range(10)]
print(list_)
dict_ = {str(j):i for j,i in enumerate(range(10))}
print(dict_)
gen = (i for i in range(10))
print(gen)
"""
# 81、举例说明SQL注入和解决办法
"""
a = "1=1"
sql = f"select * from use where {a}"
SQL注入：避免拿用户输入的参数去拼SQL
解决方法：ORM或参数校验
"""

# 82、s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
"""
str_="info:xiaoZhang 33 shandong"
new_str = re.split(r'[:\s]+',str_)
print(new_str) # ['info', 'xiaoZhang', '33', 'shandong']
"""
# 83、正则匹配以163.com结尾的邮箱
"""
email_list = ['sd.comjsdnwk@163.com', '163jhdhc@.com', 'lzynsasbndb@163.com', '23213444@163.com']
for email_ in email_list:
    ret = re.match('[\w]{4,20}@163\.com$',email_)
    if ret:
        print(f'符合：{email_}')
    else:
        print(f'不符合:{email_}')
"""
# 84、递归求和
"""
tmp_data = 1
def test(num):
    global tmp_data
    if num > 99:
        return tmp_data
    num += 1
    tmp_data += num
    return  test(num)
result = test(1)
print(result)
"""
# 85、python字典和json字符串相互转化方法
"""
str_ = 'abc123'
json_format = json.loads(srt_)
print(json_format)  # {'abc123'}
print(json.dumps(json_format)) # 'abc123'
"""
# 86、 MyISAM 与 InnoDB 区别：
"""
"""
# 87、统计字符串中某字符出现次数
"""
str_ = 'asdasd4e23rf'
print(str_.count('a')) # 2
"""
# 88、字符串转化大小写
"""
str_ = 'hello world!'
print(str_.lower()) # 小写
print(str_.upper()) # 大写
"""
# 89、用两种方法去空格
"""
str_1 = 'sda das '
print(str_1.replace(' ',''))
print(str_1.split(' '))
print(','.join(str_1.split(' '))) # 'sda,das,'
"""
# 91、简述python引用计数机制
"""
a = [1,2,3] # count =1
b = a  # count=2
del(a) #count=1
del(b) # count=0 没有变量引用这个a,python就会gc(内存清洗)
"""

# 92、int("1.4"),int(1.4)输出结果？
"""
print(int("1.4")) # invalid literal for int() with base 10: '1.4'(报错)
print(int(1.4)) # 1
"""
# 93、列举3条以上PEP8编码规范
"""
1、使用 4 个空格进行缩进，而不是制表符（Tab）。
2、每行代码的长度不应超过 79 个字符。对于注释，建议限制在 72 个字符以内。
3、在顶级函数和类定义之间使用两个空行；在类的方法定义之间使用一个空行。
4、类名使用驼峰命名法（CamelCase）;
  函数名和变量名使用小写字母和下划线（snake_case）;
  常量使用全大写字母和下划线（SCREAMING_SNAKE_CASE）。
"""
# 94、正则表达式匹配第一个URL
# 95、正则匹配中文
# 96、简述乐观锁和悲观锁
"""
"""
# 97、r、r+、rb、rb+文件打开模式区别
"""
r：读
r+：读写
rb：读二进制文件
rb+：读写二进制文件
"""
# 98、Linux命令重定向 > 和 >>
"""
>:覆盖
>>:追加
a.txt 123
echo "123" > a.txt  # 123
echo "123" >> a.txt  # 123\n123
"""
# 99、正则表达式匹配出<html><h1>www.itcast.cn</h1></html>
"""
str_ = '<html><h1>www.itcast.cn</h1></html>'
result = re.find(r'<h1><html>(.*?)</h1><html>',str_)
print(result) # 'www.itcast.cn'
"""
# 101、求两个列表的交集、差集、并集
"""
交集：集合1 & 集合2
差集：集合1 - 集合2
并集：集合1 | 集合2
"""
# 102、生成0-100的随机数
"""
print(random.randomint(1,100))
"""
# 103、lambda匿名函数好处
"""
不能用起名字，适用只用一次的场景
"""
# 104、常见的网络传输协议
"""
TCP/FTP/UDP
tcp三次握手，四次挥手
tcp和udp的区别：
1、tcp可靠连接，速度比udp慢；有三次握手，四次挥手
2、udp不可靠传输，速度快；

"""
# 105、单引号、双引号、三引号用法
"""
'' "" """"""
"""

# 106、python垃圾回收机制
"""
gc：原理是通过引用计数回收没有变量引用的数据
"""
# 107、HTTP请求中get和post区别
"""
"""
# 108、python中读取Excel文件的方法
"""
xlrd
"""
# 110、python正则中search和match