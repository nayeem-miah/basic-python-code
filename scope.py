a=100#global scope
b=50
def nayeem():
    x=10
    print(x)#local variable
    print(a)#GLOBAL VARIABLE
    global b #chenge value of global methode
    b=40
    print(b)
nayeem()

