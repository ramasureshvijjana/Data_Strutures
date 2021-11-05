class Array:
    def __init__(self, arr_len):
        self.arr_len = arr_len
        self.length = 0
        self.arr = []


    def add(self, val):
        if self.length < self.arr_len:
            self.arr.append(val)
            self.length = len(self.arr)
        else:
            print('ERROR : Array Index Out of Bound')
        

    def inserction(self, index, val):
        if self.length < self.arr_len:
            self.arr.insert(index, val)
        else:
            print('ERROR : Array Index Out of Bound')

    def updwthindex(self, index, val):
        if index < self.arr_len:
            self.arr.pop(index)
            self.arr.insert(index,val)
        else:
            print('ERROR : Array Index Out of Bound')

    def updwthvalue(self, val1, val2):
        if val1 in self.arr:
            index = self.arr.index(val1)
                    
            self.arr.pop(index)
            self.arr.insert(index,val2)
        else:
            print('val not existed')

    def delection(self, val):
        if val in self.arr:
            self.arr.remove(val)
        else:
            print('val not existed')

    def search(self, val):
        if val in self.arr:
            return self.arr.index(val)
        else:
            print('val not existed')
        

ary1 = Array(5)


print(ary1.arr)
print(ary1.length)
