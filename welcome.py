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
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Abu", "Mahfuz"]

friends.append("Abbu")
print(friends)

friends.insert(6, "Abdullah")
print(friends)
friends.reverse()


print(friends)
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends.extend(lucky_numbers)
print(friends)