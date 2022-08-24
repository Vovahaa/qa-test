def myfunc(a, b, c):
    if a > b:
        print("Great!:)")
    elif a == b:
        if c > b:
            print("You got it!:)")
        else: print("Ohh, no!:(")
    elif a < b:
        print("Ohh, No!:(")


a = int(input())
b = int(input())
c = int(input())
myfunc(a, b, c)