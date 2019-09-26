import random
number = random.randrange(0, 100)
check = "Incorrect"
print('Welcome to the random number guessing')

while check == "Incorrect":
    result = int(input("Try a value between 0 to 100"))
    try:
        val = int(result)
    except ValueError:
        print("This is a invalid number")
        continue
        val = int(result)
        if val > number:
            print("The number is greater than the actual number")
        elif val < number:
            print("The number is lower than the actual number")
            val == 0
            print("Try a number between 0 to 100")
        else:
            print("This is a correct number")
            check = "Correct"

print("Thank you")


