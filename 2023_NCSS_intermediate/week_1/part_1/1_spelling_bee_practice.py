word = input("The next word is... ")

print(word.lower())

for index in range(len(word)):
  letter = word[index]
  print(letter.upper())

print(word.lower())