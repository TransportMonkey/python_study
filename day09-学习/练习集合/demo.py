# 打印9*9的乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i}={i*j}',end=' ')
#     print()

# 打印水仙花数(例：1**3+2**3+3**3=123)
"""
1、遍历三位数
2、获取百位、十位、个位
"""
from datetime import datetime
from fractions import Fraction


# for i in range(100,1000):
#     b = i//100
#     s = i%100//10
#     g = i%10
#     if b**3+s**3+g**3 == i:
#         print(i)

# 用户输入一行字符串，分别统计字符串的英文字母、数字、其它字符的个数

# num_count = 0
# alpha_count = 0
# pace_count = 0
# other_count = 0
# str_ = input('请输入一个字符串：')
# for char in str_:
#     if char.isdigit():
#         num_count += 1
#     elif char.isalpha():
#         alpha_count += 1
#     elif char.isspace():
#         pace_count += 1
#     else:
#         other_count += 1
# print(f'含义数字字符个数：{num_count}个')
# print(f'含义英文字符个数：{alpha_count}个')
# print(f'含义空格字符个数：{pace_count}个')
# print(f'含义其它字符个数：{other_count}个')

# 给一个学生成绩信息列表，按学生的成绩进行排序
# student_info = [{'sno':'001','name':'小明','grade':98},
#                 {'sno':'002','name':'小花','grade':66},
#                 {'sno':'003','name':'小李','grade':66},
#                 ]
# grade_sort = sorted(student_info,key=lambda x:x['grade']) # 不改变原列表顺序
# student_info.sort(key=lambda x:x['grade']) # 改变原列表顺序
# print(student_info)

# 给一个整数的列表，打印该列表所有偶数的和
# even_sum = 0
# int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in int_list:
#     if num%2 == 0:
#         even_sum += num
# print(f'偶数的和为: {even_sum}')

# 创建一个字典类型，键是为姓名，值是年龄，找出年龄最大者的姓名和年龄
# list_ = [1,2,3,4]
# print(max(list_)) # sadsd
# print(max(list_,key=len)) # sadsd
# info_dict = dict([['小林',94],['小冯',44],['小李',107]])
# # print(info_dict.items())
# ret = min(info_dict.items(),key=lambda x:x[1])
# print(ret)

# 输入一个年份，判断是否为闰年
# 闰年：1、被4整除且不能被100整除 2、能被400整除
# year_ = int(input('请输入年份: '))
# if (year_%4 == 0 and year_%100 != 0) or year_%400 == 0:
#     print(f'{year_}年 是闰年~')
# else:
#     print(f'{year_}年 不是闰年~')

# 计算阶乘值   例：6   1*2*3*4*5*6
# def factorial(number:int):
#     if number > 0: # 负数没有阶乘
#         sum_ret = 1
#         for num in range(1, number + 1):
#             sum_ret *= num
#         return sum_ret
#     return '负数没有阶乘！'
# print(factorial(-45))

# 计算圆的面积
# def test(area:float):
#     return f'半径为{area}圆的面积是：{math.pi*(area**2):.2f}'
# print(test(2))

# 列表的交集、差集、并集
# a = [1,2,3,4,5,7,88]
# b = [1,2,4,5,7,53,533,55]
# def test(list_1:list, list_2:list):
#     set_= set(list_1) - set(list_2) # &交集 -差集 |并集
#     return list(set_)
# ret = test(a,b)
# print(ret)

# 计算字典的总和
# dict_ = dict([['age1',24],['age2',55],['age3',43],['age4',87]])
# def test(dic_data:dict):
#     return sum(dic_data.values())
# print(test(dict_))

# 计算偶数的倒数序列和
def test(n:int):
    ret = 0
    for i in range(1, n+1):
        if i%2 == 0 and n%2 == 0:
            ret += float(Fraction(1,i))
        else:
            if n%2 == 1:
                ret += float(Fraction(1,i))
    return ret
print(test(10))
"""
10 2 4 6 8 10
4  2 4
5 1 3
"""

# # 定义一个函数，传入年份、月份、日期,计算今天是该年的第几天
# def test(year:int, month:int, day:int):
#     current_date = datetime(year, month, day) # 年-月-日 00:00:00
#     day_of_year = current_date.timetuple().tm_yday # 'tm_yday'表示年积日
#     # print(type(current_date.timetuple())) # 返回的是一个对象（object）
#     return day_of_year # 返回年积日
# ret = test(2025, 8, 6)
# print(f'今天是今年的{ret}天')



# str_ = 'dsdsvc就会发动@$$3243'
# for char in str_:
#     if char.isdigit():
#         print('1',char)
#     elif char.isalpha():
#         print('2',char)
#     else:
#         print('3',char)





