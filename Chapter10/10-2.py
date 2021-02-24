filename = "learning_python.txt"

with open(filename) as file_object:
    for line in file_object.readlines():
        print(line.rstrip().replace("Python", "C"))