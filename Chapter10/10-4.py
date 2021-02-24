filename = "guest_book.txt"

while True:
    username = input("Please input your name(enter n if you want to end it): ")
    if username == 'n':
        break
    print("Hello, " + username.title())
    with open(filename, 'a') as file_object:
        file_object.write(username + "\n")

