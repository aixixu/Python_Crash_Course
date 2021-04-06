name_place = {}
active = True
while active:
    name = input("What's your name?")
    place = input("If you could visit one place in the world, where would you go?")

    name_place[name] = place

    repeat = input("Would you like to let another person respond? (yes or no) ")
    if repeat == 'no':
        active = False

print("\n--- Results ---")
for name, palce in name_place.items():
    print(f"{name.title()} would like to visit {palce.title()}.")  