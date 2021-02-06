def make_album(singer_name, album_name, numbers=''):
    album = {'singer': singer_name, 'album': album_name}
    if numbers:
        album['number of songs'] = numbers
    return album

while True:
    print("\nPlease input the information of your album: ")
    print("(enter 'q' if you want to quit)")
    singer_name = input("Please input the singer name: ")
    if singer_name == 'q':
        break

    album_name = input("Please input the album name: ")
    if album_name == 'q':
        break

    print(make_album(singer_name,album_name))