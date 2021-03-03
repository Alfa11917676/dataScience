'''def recursion(n):
    listRange=[1,2,3,4,5]
    range=len(listRange)
    if n>range:
        exit()
    if n>=3:
        print(listRange[n-1])

    recursion(n+1)
recursion(1)
from random import shuffle
listRange=[1,2,3,4,5]
randomized=shuffle(listRange)
print(randomized)
if __name__ == '__main__':
    from multiprocessing import Process
    def suareroot(num=12):
        for i in range(101001111):
            pass
        print(num**num,",",i,",",num)
    proc=[]
    for i in range(10):
        proc.append(Process(target=suareroot()))
    for processed in proc:
        processed.start()
    print("Hello World!!!!!")
'''
from threading import  *
if __name__ == '__main__':
    def squ(n):
        print(n**2)
    def cube(n):
        print(n**3)
    t1=Thread(target=squ,args=[4])
    t2=Thread(target=cube,args=[4])
t1.start()
t2.start()
print("he")