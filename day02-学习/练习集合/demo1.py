# 封装与解构
a,b = 4,5 # 右边封装元组类型(4,5),为了赋值给a,b,解构后，依次对应标识符
print(a,b)
c,d = 'bd'
print(c,d)
e,f = {7,8} # 集合没有顺序
print(e,f)
g,*h = range(10) # *h代表是剩余变量,尽可能收集更多的数据
print(g,h)
j,*w,h = range(10)
print(j,w,h) # 0 [1, 2, 3, 4, 5, 6, 7, 8] 9

