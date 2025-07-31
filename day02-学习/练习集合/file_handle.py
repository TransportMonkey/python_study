"""
实现一个可以统计文件有效行数的上下文管理器
"""
class CountLine:
    def __init__(self, file_name:str, mode:str):
        self.file_name = file_name
        self.mode = mode
    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        print('Opened file!')
        return self # 这里为什么要返回self?
    def __exit__(self, exc_type, exc_val, exc_tb):
        get_line = self.read_file()
        if get_line > 0:
            print(f'{self.file_name.split(".")[0]}文件统计有效行数：{get_line}行')
            print('Close file!')
            self.file.close()
    def read_file(self):
        line = 0
        for l in self.file:
            stripped = l.strip()
            if stripped and not stripped.startswith('#'):
                line += 1
        return line
with CountLine('abc.txt','r') as file:
    pass