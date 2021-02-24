filename = 'guest.txt'

with open(filename, 'w') as file_object:
    username = input("Please input your name: ")
    file_object.write(username)