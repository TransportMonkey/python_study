import os,threading,time,random,re
import requests,subprocess
from datetime import datetime, timedelta

# 1、（os模块）编写函数统计指定目录下所有.txt结尾文件的总大小（忽略子目录）
def total_file_size(dst_dir):
    """
        os.listdir(文件夹路径) 遍历当前目录
        os.path.getsize(文件路径)  得到单个文件的大小
        os.path.join(当前目录路径, 目标文件) 把目录路径和目标文件拼接成一条完整有效的路径
        sum(元组类型数据) 统计数据大小
    """
    if not os.path.exists(dst_dir):
        print(f'0kb')
        return
    find_dst_file = [file for file in os.listdir(dst_dir) if file.endswith(".txt")] # 得到当前目录所有文件
    all_file_size = tuple(os.path.getsize(os.path.join(dst_dir, file)) for file in find_dst_file) # (32,54435,7657,65,)
    get_total_size = sum(all_file_size)
    print(get_total_size)
    # 新增：字节自动转 KB/MB/GB
    """
    1Byte(字节) = 8bit(比特)
    1MByte兆 = 1024KByte
    1M = 1024K
    1GB = 1024M = 1024 * 1024K
    """
    # get_total_size = 16472/
    for unit in ['B', 'KB', 'MB', 'GB']:
        if get_total_size < 1024.0:
            break
        get_total_size /= 1024.0 # get_total_size = get_total_size / 1024 = 16.
    print(f'Total file size: {get_total_size:.2f} {unit}')
total_file_size('random_files')
# 2、（datetime模块）计算当前时间到N天前的当前时间之间工作日的天数（不考虑节假日）
N = 7 # 假设是7天前
curr_time = datetime.now() # 获取当前具体时间
start_day = curr_time - timedelta(days=N) # 日期做加减运算
def count_weekdays_between(start_date, end_date):
    """计算两个日期之间的工作日数量（不含节假日）"""
    if start_date > end_date:
        start_date, end_date = end_date, start_date  # 保证 start <= end
    weekday_count = 0 # 统计工作日
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:  # 周一到周五为 0-4
            weekday_count += 1
        current_date += timedelta(days=1)
    return weekday_count
# now = datetime.now()
# print(now.weekday())
# 计算工作日天数
weekdays = count_weekdays_between(start_day, curr_time)
print(f"从 {start_day.strftime('%Y-%m-%d %H:%M:%S')} 到 {curr_time.strftime('%Y-%m-%d %H:%M:%S')} 之间有 {weekdays} 个工作日（不含节假日）")



# 3、（threading模块）实现多线程下载器（模拟下载3个URL）
a = 0
url = ['https://dsbdsdbxc.com','https://fertretgh.com','https://gfdgffg.com']*1000
def simulate_download(url:str):
    global a
    """
    threading.current_thread().name 获取当前线程名称
    """
    print(f"[{threading.current_thread().name}] 开始下载 {url}")
    time.sleep(random.randint(1, 9))
    print(f"[{threading.current_thread().name}] 完成下载 {url}")
    a+=1
def th_run():
    task = []
    for ul in url:
        t = threading.Thread(target=simulate_download, args=(ul,))
        task.append(t)
        t.start()
    for t in task:
        t.join()
        # t.join() # 主线程会卡在这里，直到上一个线程结束

# th_run()
# print(a)

# 4、（multiprocessing模块）用进程池计算1000000以内素数的个数（对比单进程速度）



# 5、(requests模块) 获取网页(https://www.python.org/)内容并保存到文件
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}
def get_html_data(py_url:str):
    # 发送 GET 请求
    resp = requests.get(py_url, headers=headers, timeout=10)
    resp.raise_for_status() # 查看状态码 200(成功) 400(bad requests) 404(No found) 500(server err) 502(bad gateway) 503(Service Unavailable)
    print(f'-----获取网页数据成功！---------')
    return resp.text
def save_html_content(py_url:str):
    data = get_html_data(py_url)
    with open('python_html.txt','w',encoding='utf-8') as f:
        f.write(data)
    print(f'------文件保存成功！---------')

# save_html_content('https://www.python.org/')

# 6、（re模块）写一个函数，接收一个邮箱，通过正则表达式验证邮箱格式是否正确，返回bool值
def is_valid_email(email:str):
    """
    email有效格式：用户名@域名.后缀
    用户名允许：字母（a-z/A-Z）、数字（0-9）、点（.）、下划线（_）、百分号（%）、加号（+）、减号（-）
              不能连续出现两个点（如a..b@无效）
              首尾不能是点（如.a@或a.@无效） ----- 字符集(^[a-zA-Z0-9._%+-]+)
    @：必须且只能有一个                     ----- 一个实实在在的 @ 符号，分隔用户名与域名。
    域名：至少包含一个点（如example.com）
         域名和后缀只能包含字母、数字和连字符（-） --------   [a-zA-Z0-9.-]+
    后缀：长度至少2位（如.cn、.com、.net）------ [a-zA-Z]{2,}
    """
    pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    """
    re.compile(正则式表达字符串类型)：
    $: 表示“匹配到字符串末尾”，保证整个字符串都符合规则，没有多余字符。
    \.: 一个真正的点号（在正则里 . 本来表示“任意字符”，所以前面加反斜杠 \ 转义成普通点号）。
    """
    return bool(pattern.fullmatch(email))
# email_str = 'sdsf453454t@qq.com'
# res = is_valid_email(email_str)
# print(f'{res}')

# 7、（subprocess模块）执行系统命令（ipconfig）并打印命令输出结果
"""
subprocess模块：专门用来“生”一个新的进程去执行系统命令。
"""
# result = subprocess.run('ipconfig', capture_output=True, text=True, check=True)
# print(result.stdout)          # 标准输出
# print(result.stderr, end='')  # 标准错误（一般没有）
