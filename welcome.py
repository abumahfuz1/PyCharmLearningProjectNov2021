employee_file = open("test.txt", "r") #to replace or re write on the older file use w
employee_file = open("test.txt", "a") #to apend the txt file
employee_file.write("\nToby - Human Resources")

employee_file.close()

#print(employee_file.read())


employee_file = open("index.html", "w") #to replace or re write on the older file use w

employee_file.write("<p>This is HTML Code</p>")

employee_file.close()

    #reader = csv.reader(f)
    #for row in reader:
      #  print(row)