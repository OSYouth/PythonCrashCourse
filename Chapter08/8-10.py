def make_great(magicians):
    count = 0
    for count in range(0, len(magicians)):
        temp = "the Great " + magicians[count]
        magicians[count] = temp

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ['Tom', "Leo", "Kagura"]
make_great(magicians)
show_magicians(magicians)