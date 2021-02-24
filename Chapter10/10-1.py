filename = "learning_python.txt"

with open(filename) as file_object:
    print(file_object.read())

with open(filename) as file_object:
    for line in file_object.readlines():
        print(line.strip())

with open(filename) as file_object:
    lines = file_object.readlines()
for l in lines:
    print(l.strip())