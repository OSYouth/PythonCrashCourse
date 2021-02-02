favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

# for name in favorite_languages.keys():
for name in sorted(favorite_languages):
    print(name.title() + ",thank you for taking the poll.")
