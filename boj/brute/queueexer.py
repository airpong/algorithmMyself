class queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.allarray = [0]*1000
    def push(self,lst):
        self.rear+=1
        self.allarray[self.rear]=lst
    def pop(self):
        if self.front==self.rear:
            return False
        self.front+=1
        return self.allarray[self.front]

a = queue()
a.push(2)
a.push(3)
a.push(4)
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
b = queue()
b.push(3)
print(b.pop())
del a
a.push(3)