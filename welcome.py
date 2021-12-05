print("#### Try Except block ---Error / Exception Handing ######")
try:
    #value = 10/0
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError as err :
    print("Divided by zero")
except ValueError:
    print("Invalid Input")
