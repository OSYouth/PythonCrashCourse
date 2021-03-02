def print_animal_name(filename):
    """打印动物名字"""

    try:
        with open(filename) as f_obj:
            names = f_obj.readlines()
    except FileNotFoundError:
        print("File not found.")
    else:
        for name in names:
            print(name.strip().title())

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print_animal_name(filename)