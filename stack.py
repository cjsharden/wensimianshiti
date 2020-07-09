import numpy as np

#a使用类的封装思想，封装一个双端栈
class stack:
    # 初始化栈
    def __init__(self):
        self.a = np.array([None] * 5)
        self.l = -1 #定义左边栈指针
        self.r = len(self.a)  #定义右边栈指针
    #判断栈空
    def is_emptyl(self):
        if self.l == -1:
            return True
        else:
            return False
    def is_emptyr(self):
        if self.r == len(self.a):
            return True
        else:
            return False
    #判断栈满
    def is_full(self):
        if self.l+1 == self.r:
            return True
        else:
            return False
    #走边栈操作
    def l_push(self,datal):
        if self.is_full():
            print("栈满，不能进栈")
        else:
            self.l += 1 #先移动指针，在进栈
            self.a[self.l]=datal

    def l_pop(self):
        if self.is_emptyl():
            print("栈空，不能出栈")
        else:
            popdatal = self.a[self.l]  #先出栈，在移动指针
            self.l -=1
            return popdatal
    #右边栈操作除了使用尾指外，其他同理
    def r_push(self,datar):
        if self.is_full():
            print("栈满，不能进栈")
        else:
            self.r -=1
            self.a[self.r]=datar
    def r_pop(self):
        if self.is_emptyr():
            print("栈空，不能出栈")
        else:
            popdatar = self.a[self.r]
            self.r +=1
            return popdatar
