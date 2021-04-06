age = "\nHello, how old are you?"
age += "\n Enter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(age)
    if message == 'quit':
        pass
    elif int(message) < 3:
        print("your are free")
    elif int(message) >= 3 and int(message) <= 12:
        print("$10")
    elif int(message) > 12:
        print("$15")
    
