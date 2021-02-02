favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

investigated_persons = ['osyouth', 'jen', 'eric', 'edward']

for person in investigated_persons:
    if person in favorite_languages.keys():
        print(person.title() + ", thanks for your investigating!")
    else:
        print(person.title() + ", please take the survey.")