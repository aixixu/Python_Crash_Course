favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

name_list = ['jen','cohen','ethan','sarah','emma','edward','cowan','phil']

for name in name_list:
    if name in favorite_languages.keys():
        print(f"{name.title()}\n\tThanks for participating in this survey!")
    else:
        print(f"{name.title()}\n\tWelcome to participate in this survey!")