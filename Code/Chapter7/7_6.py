ingredient = "\nAdd ingredient:"
ingredient += "\n Enter 'quit' to end the program."

active = True
while active:
    message = input(ingredient)
    if message == 'quit':
        active = False
    else:
        print(f"we will add {message} to your pizza")

while True:
    message = input(ingredient)
    if message == 'quit':
        break
    else:
        print(f"we will add {message} to your pizza")

age = "\nHello, how old are you?"
age += "\n Enter 'quit' to end the program."

active = True
while active:
    message = input(age)
    if message == 'quit':
        active = False
    elif int(message) < 3:
        print("your are free")
    elif int(message) >= 3 and int(message) <= 12:
        print("$10")
    elif int(message) > 12:
        print("$15")
    
while True:
    message = input(age)
    if message == 'quit':
        break
    elif int(message) < 3:
        print("your are free")
    elif int(message) >= 3 and int(message) <= 12:
        print("$10")
    elif int(message) > 12:
        print("$15")
    
