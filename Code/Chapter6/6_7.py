AixiXu = {
    'first_name': 'aixi',
    'last_name': 'xu',
    'age': 23,
    'city': 'nanchang',
    }

Cohen = {
    'first_name': 'cohen',
    'last_name': 'steve',
    'age': 20,
    'city': 'London',
}
Ethan = {
    'first_name': 'ethan',
    'last_name': 'joe',
    'age': 26,
    'city': 'Waston',
} 
members = [AixiXu,Cohen,Ethan]
for member in members:
    print(f"{member['first_name']} {member['last_name']}'s age is {member['age']} and living in {member['city']}")

