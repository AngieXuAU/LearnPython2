colour = input("Which colour did you find? ")
number = int(input("Number of tins: "))

colour = colour.lower()

if "blue" in colour:
  print("Excellent! We'll soon have enough paint for the sky!")
elif number < 4:
  print(f"We're running out of {colour} paint. Let's restock!")
else:
  print(f"Great! We have {number} tins of {colour} paint.")


