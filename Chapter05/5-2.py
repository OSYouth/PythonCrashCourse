str1 = 'Long'
str2 = 'Short'
print(str1 == str2)

print(str1.lower() == 'long')

num1 = 10
num2 = 20
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

print(num1 > num2 and num1 < num2)
print(num1 > num2 or num1 < num2)

names = ['Leo', "Tom"]
if "Leo" in names:
    print("Leo is in the list.")

if "Jerry" not in names:
    print("Jerry is not in the list.")