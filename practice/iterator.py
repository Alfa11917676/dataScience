class initializer:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return new_class(self.n)
class new_class:
    def __init__(self,n):
        self.n=n
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.n>self.i:
            i=self.i
            self.i+=1
            return i
        else:
            raise StopIteration()
for integers in initializer(10):
    print(integers**2)