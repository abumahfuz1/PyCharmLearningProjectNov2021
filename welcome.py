coordinates = [(4,5), (6,7), (80, 34)]
coordinates[1] = 10
print(coordinates [1])


print("#### Functions  ######")
def translate(phrase):
    translation = " "
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + " G "
            else:
                translation = translation + letter + "g"
        else:
            translation = translation + letter
    return translation
print((translate((input("Enter a phrase: ")))))