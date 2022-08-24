def myfunc(a, b, c):
    if a >= b: print("We are out of task")
    while a < b:
        print(a)
        a += c
        if a >= b:
            print(a)
            #break


a = int(input())
b = int(input())
c = int(input())
myfunc(a, b, c)