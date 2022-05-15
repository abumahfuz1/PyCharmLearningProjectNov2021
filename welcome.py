
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
print("")
print("###########BINARY VALUE##############")
print("")
a=0b10011111
b=0b11101100
c=0b1111100

print("Binary value for a 0b101 - a is" , a)
print("Binary value for a 0b101 - b is" , b)
print("Binary value for a 0b101 - c is" , c)

print("")
print("########### OCATAL VALUE##############")
print("")
#Base value 8
#Accepts values from 0-7
#prefix for Ocatal is 0o
a=0o01234567
print("Octal value for 0o123 -a is", a)


print("")
print("###########HEXA DECIMAL VALUE##############")
print("")
#Base value 16
#Accepts values from 0-9 and a to f (total 16)
#Accept alphabets from a to f or A to F (6 alphabest)
#prefix for Ocatal is 0x or 0X

a=0xface
b=0xabcd
c=0xfedcba
print("Hexa Decimal value for 0xface is ", a)
print("Hexa Decimal value for 0xabcd is ",b)
print("Hexa Decimal value for 0xfedcba is " ,c)

print("")
print("###########DECI-OCTA-HEXA DECIMAL VALUE##############")
print("")
Decimal=10
Binary=0b11
Octal=0o674
Hexa=0x6748
print("Base value for Decimal form is ", Decimal)
print("Base value for Binary form is ", Binary)
print("Base value for Octal form is ", Octal)
print("Base value for Hexa form is ", Hexa)


print("")
print("#########  RELATIONAL OPERATOR ##############")
print("")
#==, !=, <, >, <=, >=
A=100 #DS
B=200
print("a=b is: " ,a==b)


print("")
print("######### ASSIGNMENT OPERATORS  ##########")
print("")
#=-> Assignment Operators
#== Comparison Operators
#+= add and assign
a=100
print("Before assigning-adding value of b ", a)
b=20
a+=b #a=> a+b
print("After adding value of b to a", a)


#-= subtract and assign
a=300
print("Before assigning-subtracting value of b ", a)
a-=b  #a=> a-b
print("After subtracting value of b to a", a)

#*= Multiply and assign
a=25
print("Before assigning-multiplying value of b ", a)
a*=b  #a=> a-b
print("After multiplying value of b to a", a)


#/= Devide and assign
a=25
print("Before assigning-deviding value of b ", a)
a/=b  #a=> a-b
print("After deviding the value of b to a", a)

print("")
print("######### LOGICAL EXPRESSION  ##########")
print("")

a=20
b=21
print("a>b or a=b: ", a>b or a==b)

a=20
b=21
print("a<b or a=b: ", a<b or a==b)

print("")
print("#########  IN - NOT IN MEMBERSHIP OPERATOR  ##########")
print("")

#True or False
#1. in
#2. Not in
#to check the value in the object
#if existed then it will return True
#if not existed then it will return False

x="PYTHEON"
print("H" in x)
print("h" in x)

A=[90,89,30,40]

A=[90,89,30,40]
print(A)
print(type(A))
print(90 not in A)
