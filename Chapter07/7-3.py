number = input("Enter a number, and I'll tell you it's times of 10: ")
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is times of 10.")
else:
    print("\nThe number " + str(number) + " is not times of 10.")