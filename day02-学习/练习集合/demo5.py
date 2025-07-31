import json
a = [1,2,3]
b = json.dumps(a)
print(type(b))
c = json.loads(b)
print(c,type(c))

A = {"test方法":1,"test2":2}
B = json.dumps(A,ensure_ascii=False) # '{"test":1,"test2":2}'
print(type(B),B)
C = json.loads(B)
print(C,type(C))


def test(t,*args,a=True,**kwargs):
    print(args)
    print(t)
    print(a)
    print(kwargs)

    e = kwargs.get("e")
    print(e)

test(1,2,4,5,6,7,8,9,a=True,b=False,c=4,d=5,e=6)