favorite_number = {
    'cohen' : [99,101],
    'emma' : [3,4,9,67],
    'mason' : [888,5,666],
    'karre' : [1,10930],
    'ethan' : [321],
}

for key,value in favorite_number.items():
    print(f"{key.title()}'s favorite palces is",end="")
    for i in range(len(value)):
        if i < len(value)-1:
            print(f" {value[i]},",end="")
        else:
            print(f" {value[i]}.")
