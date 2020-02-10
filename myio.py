#three data types at input

#string
phrase = input ("Enter a string: ")
print ("You said " + phrase)
print (f"You said {phrase}")

#float
someFloat = float(input("Enter a float: "))
print ("You enetered float: " + str(someFloat))
print (f"You entered float: {someFloat}"))

#int
someInt = float(input("Enter an int: "))
print ("You entered int: " + str(someInt))
print (f"You entered int: {someInt}")

#string interpolation
print(f"Do python inline, like this: {someFloat} * {someInt} = {someFloat * someInt}")
