def make_great(magicians):
    count = 0
    for count in range(0, len(magicians)):
        temp = "the Great " + magicians[count]
        magicians[count] = temp
    return magicians

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ['Tom', "Leo", "Kagura"]
magicians_copy = make_great(magicians[:])
show_magicians(magicians)
show_magicians(magicians_copy)