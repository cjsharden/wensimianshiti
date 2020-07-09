class HashTable:
    #初始化127个acsii码的哈希表
    def __init__(self):
        self.index = [i for i in range(127)]  # 创建哈希索引
        self.val = [None] * 127  # 创建哈希值
        self.mod = 127
        self.table = []
    #创建哈希表
    def creat_hash(self,datas):
        for data in datas:
            h_index = data % self.mod
            if self.val[h_index] is None:
                self.val[h_index] = data
            else:  # 处理冲突（采用线性探测再散列）
                while self.val[h_index] is not None:
                    if (h_index + 1) >= len(self.val):# 超出hash表长度时，从头散列
                        h_index = -1
                    h_index += 1
                self.val[h_index] = data
    def get(self,num):
        h_index = num%self.mod
        while self.val[h_index]!=num:
                if (h_index+1) >=len(self.val):
                    h_index =-1
                h_index+=1
        print(self.index[h_index])
    def outhash(self):
        print(self.val)
        print(self.index)
if __name__=='__main__':
    test = [127,58,59,8,5]#测试集0~127内的ascii码
    h=HashTable()
    h.creat_hash(test)
    h.get(58)


