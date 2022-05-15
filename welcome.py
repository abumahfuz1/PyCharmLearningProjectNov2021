


a=10 #decimal
print(a)
print(type(a))

#function creation
b=100
c="Test"
def f1():
    print("Global variable for f1-b is," ,b)

#Function calling
f1() #this will provide the result of b value



a=12 #Global
def f1():
    print("Global variable for f1 -a is, " ,a)
def f2():
    print("Global variable for f2 -c is, " ,c)
def f3():
    print("Global variable for f3 -b is, ", b)

def f4():
        p = 17
        print("Local variable for f4 -a is", p)


f1()
f2()
f3()
f4()


#Binary
a=0b10011111
b=0b11101100
c=0b1111100

print("Binary value for a 0b101 - a is" , a)
print("Binary value for a 0b101 - b is" , b)
print("Binary value for a 0b101 - c is" , c)