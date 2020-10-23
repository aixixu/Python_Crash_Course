favorite_places = {
    'aixi':['British Museum','Blenheim Palace','Palace of Westminster'],
    'cohen':['Tower of London'],
    'ethan':['TowerBridge','BigBen'],
}

for key,value in favorite_places.items():
    print(f"{key.title()}'s favorite palces is",end="")
    for i in range(len(value)):
        if i < len(value)-1:
            print(f" {value[i].title()},",end="")
        else:
            print(f" {value[i].title()}.")

