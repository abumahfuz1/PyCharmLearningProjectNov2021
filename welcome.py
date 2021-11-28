
def school_age_calculator(age,name):


    if age < 5:
        print("Enjoy the time!", name, "is only", age)
    elif age == 5:
        print("Ejnoy Kindergarten,", name)
    elif age ==7:
        print("Enjoy second grade!")

    else:
        print("they gow up so fast!")
school_age_calculator(7, "Rahma")

print("####################################")
print("####################################")
print("          ")
print("MyAge")
print("          ")
####My Age
def add_ten_to_age(age):
    new_age = age +10
    return new_age

How_Old_Will_I_Be = add_ten_to_age(20)
print(How_Old_Will_I_Be)

print("####################################")
print("####################################")
print("          ")
print("While Loop")
print("          ")
x=0
while (x<5):
    print(x)
    x=x+1

    #For
    for x in range(5,10):
        print(x)

        days=["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]
        for d in days:
            print(d)
