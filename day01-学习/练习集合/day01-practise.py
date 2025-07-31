"""列表推导式练习"""
# 取1~10之间的每个元素平方数(用列表推导式实现)
res_1 = [i**2 for i in range(1,11)]
print(res_1)
# 取1~10之间的质数(列表推导式实现)
res_2 = [i for i in range(2, 11) if all(i % j for j in range(2, i))]
print(res_2)          # [2, 3, 5, 7]
#生成一个包含1到100间所有偶数的列表(使用列表推导式实现)
res_3 = [i for i in range(1,101) if i%2 == 0]
print(res_3)
# 生成一个包含1到100之间所有奇数的平方,偶数不变的列表(使用列表推导式实现)
res_4 = [i**2 if i%2 == 1 else i for i in range(1,101)]
print(res_4)
# 给定一个字符串列表 words = ["apple", "banana", "cherry"]，生成一个新列表，包含每个单词的大写形式。
words_1 = ["apple", "banana", "cherry"]
res_5 = [i.upper() for i in words_1]
print(res_5)
# 给定一个字符串列表 words = ["python", "java", "c++", "go"]，生成一个新列表，只保留长度大于3的字符串，并将它们转为小写。
words_2 = ["Pyhon", "Java", "c++", "go"]
res_6 = [i.lower() for i in words_2 if len(i) > 3]
print(res_6)
# 给定一个列表 matrix = [[1, 2], [3, 4], [5, 6]]，将其展平为一个一维列表。
matrix = [[1, 2], [3, 4], [5, 6]]
res_7 = [j for i in matrix for j in i]
print(res_7)
# 给定一个列表 nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，生成一个新列表，只保留能被3整除的数的平方。
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res_8 = [i**2 for i in nums if i//3]
print(res_8)
# 给定一个字符串 s = "Hello 123 World 456"，生成一个列表，包含其中所有的数字字符。
s = "Hello 123 World 456"
res_9 = [i for i in s if i.isdigit()]
print(res_9)
# 生成一个包含1到100之间所有质数的列表(使用列表推导式实现)
res_10 = [i for i in range(2,101) if all(i%j for j in range(2,i))]
print(res_10)

"""生成器练习"""
'''
实现一个生成器函数 answer_checker(answer_list)：
输入：标准答案列表（如 ['A', 'B', 'C', 'D']）
生成值：每次返回对应题号的答案（格式："题号-答案"）
特性：支持无限题号（如答案用完后循环使用）
'''
def answer_generator(answer_list):
    index = 0
    while True:
        yield f"{index + 1}-{answer_list[index % len(answer_list)]}"
        # for ans in answer_list:
        #     yield f'{num}-{ans}'
        #     num += 1
        index += 1
gen = answer_generator(['A','B','C','D'])
print(next(gen)) # 1-A
print(next(gen)) # 2-B
print(next(gen)) # 3-C
print(next(gen)) # 4-D
print(next(gen)) # 5-A
print(next(gen)) # 6-B
print(next(gen)) # 7-C
gen2 = answer_generator(['a','b','c','d'])
print(next(gen2)) # 6-B
print(next(gen2)) # 7-C
print(next(gen2)) # 8-D

"""装饰器练习"""
import time
# 装饰器的定义，写一个装饰器（timer），实现函数执行时间计算
def timer(orig_func):
    def original_timer(*args,**kwargs):
        start_time = time.perf_counter() # 开始计时cpu时间
        orig_func(*args,**kwargs)
        end_time = time.perf_counter() - start_time
        print(f'{orig_func.__name__}耗时: {end_time:.3f}s')
    return original_timer
#@timer
#peace_request = timer(peace_request)
@timer
def peace_request():
    total = sum(range(1, 1000000001))
    print(total)  # 输出 5050
peace_request()

"""上下文管理器"""
# 计时器上下文管理器
class Timer:
    def __init__(self):
        self.time_lag = 0
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.time_lag = self.end - self.start
        return False
with Timer() as timer:
    tmp_data = []
    for i in range(5000):
        tmp_data.append(i**2)
print('--232---')
print(f'耗时：{timer.time_lag:.3f}s')
# 文件上下文管理器
class SafeFile:
    def __init__(self, filename:str, mode:str):
        self.file_name = filename
        self.mode = mode
    def __enter__(self):
        # 判断文件存不存在
        if os.path.exists(self.file_name):
            # 文件存在，先拷贝
            new_file_name= f"{self.file_name}.20250729-210000"
            shutil.copyfile(self.file_name,new_file_name)
        # current_time = time.localtime()
        # formatted_time = time.strftime("%Y%m%d-%H:%M:%S", current_time)
        # self.backup_file_name = f'{self.file_name}_{formatted_time}{}'
        # with open()
        self.file = open(self.file_name, mode=self.mode)
        print('Open ', self.file_name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            # # 获取当前时间
            # current_time = time.localtime()
            # # 格式化为 20250729-12:00:00 的形式
            # formatted_time = time.strftime("%Y%m%d-%H:%M:%S", current_time)
            # self.file_name = f'{self.file_name}_{formatted_time}'
            self.file.close()
            print('Close ', self.file_name)
    def write(self, answer_list: str):
        self.file.write(answer_list)


with SafeFile('noe.txt','w') as file:
    file.write("1234567")