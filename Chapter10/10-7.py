print("Give me two numbers, and I'll sum them up.")
first_number = input("\nFirst number: ")
second_number = input("Second number: ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Please enter two numbers instead of text.")
else:
    print(answer)