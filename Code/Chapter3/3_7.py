names = ['cohen','ethan','jamie']
print(f'{names[0].title()}, welcome to my dinner!')
print(f'{names[1].title()}, welcome to my dinner!')
print(f'{names[2].title()}, welcome to my dinner!')
    
print(f'\n{names[1].title()} cannot keep our engagement.')
names[1]='mason'
print(f'\n{names[0].title()}, welcome to my dinner!')
print(f'{names[1].title()}, welcome to my dinner!')
print(f'{names[2].title()}, welcome to my dinner!')

print('\nI have a bigger table!')
names.insert(0, 'aixi')
print(names)
names.insert(2, 'steve')
names.append('ashe')
for name in names:
    print(f"{name.title()}, welcome to my dinner!")

print("\nI'm sorry, because the table cannot be served on time, I can only invite two guests to dinner.")
while len(names) > 2:
    sorry_name = names.pop()
    print(f"{sorry_name}, I'm sorry I can't invite you to dinner. Maybe next time") 
for name in names:
    print(f"{name.title()}, welcome to my dinner!")
del names[0]
del names[0]
print(names)