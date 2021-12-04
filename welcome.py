print("  ### LIst ###   ")
friends = ["Kevin", "Karen", "Jim", "Abu", "Mahfuz"]
print(friends)
#print(friends[1:3])
#print(friends[1:2])

friends[0] = "Saleh" #replaces value 0 Kevin to Saleh
print(friends[0])
print(friends[2])
print(friends[-1])

print("  ### List ###   ")
lucky_numbers = [45, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Abu", "Abu", "Mahfuz"]

friends.append("Abbu")
print(friends)

friends.insert(6, "Abdullah")
print(friends)
friends.reverse()


print(friends)
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends.remove("Abdullah")
print(friends)

#lucky_numbers.clear()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends.extend(lucky_numbers)
print(friends)
#lucky_numbers.clear()
#friends.clear()
print(friends)

friends.pop() #removes last element
print(friends)

print((friends.index("Kevin")))
print(friends.count("Abu"))
