countries = ['china','uk','usa','japan','germany','franch']
for country in countries:
    print(f'{country.title()} ', end='')
countries[2]='korea'
print('\n')
for country in countries:
    print(f'{country.title()} ', end='')
countries.append('india')
print('\n')
for country in countries:
    print(f'{country.title()} ', end='')
countries.insert(0,'ireland')
print("\nInsert at the head of the list.")
for country in countries:
    print(f'{country.title()} ', end='')
countries.insert(4,'netherland')
print("\nInsert at the fifth position of the list.")
for country in countries:
    print(f'{country.title()} ', end='')   
print(f"\n{countries.pop()} is popped.")
for country in countries:
    print(f'{country.title()} ', end='')
print(f"\nThe third element, {countries.pop(2)}, is popped.")
for country in countries:
    print(f'{country.title()} ', end='')
del countries[-1]
print("\nThe last element in the list has been deleted.")
for country in countries:
    print(f'{country.title()} ', end='')
countries.remove('ireland')
print("\nIreland has been deleted.")
for country in countries:
    print(f'{country.title()} ', end='')
print("\nThe original list:" , end='')
for country in countries:
    print(f'{country.title()} ', end='')
print("\nUsing sorted fuction:" , end='')
sorted(countries)    
for country in countries:
    print(f'{country.title()} ', end='')
print("\nUsing reverse method:" , end='')    
countries.reverse()
for country in countries:
    print(f'{country.title()} ', end='')
print("\nThe original list:" , end='')
countries.reverse()
for country in countries:
    print(f'{country.title()} ', end='')
print("\nUsing sort method:" , end='')    
countries.sort()
for country in countries:
    print(f'{country.title()} ', end='')
print("\nreverse:" , end='')    
countries.sort(reverse=True)
for country in countries:
    print(f'{country.title()} ', end='')
print('\n')
print(len(countries))
