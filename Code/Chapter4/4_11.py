my_pizzas = ['durian pizza','pepperoni pizza','margherita pizza']
friend_pizzas = my_pizzas[:]
my_pizzas.append('hawaiian fruit pizza')
friend_pizzas.append('potato fruit Pizza')
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title(),end='/ ')
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title(),end='/ ')
