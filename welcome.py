test_file = open("test.txt", "r")  #to read the txt file
print(employee_file.read())
employee_file.close()

#employee_file = open("test.txt", "w") #to replace or re write on the older file use w
employee_file = open("test.txt", "a") #to apend the txt file
employee_file.write("\nToby - Human Resources") #to add a new employee to HR







    #reader = csv.reader(f)
    #for row in reader:
      #  print(row)