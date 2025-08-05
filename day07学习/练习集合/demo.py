class Demo:
    name = 'haha'
    def test(self):
        # print(self.name)
        print(Demo().__class__) # <class '__main__.Demo'>
print(Demo.__class__) #
demo = Demo()
demo.test()
print(demo)