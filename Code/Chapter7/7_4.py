ingredient = "\nAdd ingredient:"
ingredient += "\n Enter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(ingredient)
    if message == 'quit':
        pass
    else:
        print(f"we will add {message} to your pizza")