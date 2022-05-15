
a=10
print(a)
print(type(a))

#function creation
b=100
c=50
def f1():
    print("Global variable is," ,b)

#Function calling
f1() #this will provide the result of b value

a=12 #Global
def f1():
    print("Global variable is, " ,a)
def f2():
    print("Global variable is, " ,c)
f1()
f2()
