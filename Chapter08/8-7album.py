def make_album(singer_name, album_name, numbers=''):
    album = {'singer': singer_name, 'album': album_name}
    if numbers:
        album['number of songs'] = numbers
    return album

album = make_album('xtf', '因为爱所以爱')
print(album)
album = make_album('wf', '匆匆那年')
print(album)
album = make_album('毛不易', '消愁', 5)
print(album)
