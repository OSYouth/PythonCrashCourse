users = ['admin', 'test', 'lc', 'osyouth', 'ymqc']
# del users[:5]
# users.pop()
users.remove("lc")
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report.")
        else:
            print("Hello " + user + ", thank you for logging in again.")
else:
    print("We need to find some users!")

