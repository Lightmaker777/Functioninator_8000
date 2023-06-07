word = input("Enter the word: ")
if word[-1] in "bcdfghjklmnpqrstvwxyz":
    result = word + "inator " + str(len(word) * 1000)
else:
    result = word + "-inator " + str(len(word) * 1000)

print(result)
