Cohen = {
    'pets_type': 'cat',
    'master': 'Aixi',
}
Ethan = {
    'pets_type': 'dog',
    'master': 'Aixi',
} 
Joe = {
    'pets_type': 'dog',
    'master': 'David',
} 
pets = [Cohen,Ethan,Joe]
for pet in pets:
    print(f"{pet['master']}'s pet is a {pet['pets_type']}.")

