pizzas = ['muzzarella', 'fugazzetta', 'napolitana', 'caprese', 'fugazza']
friend_pizzas = pizzas[:]

pizzas.append('pesto')
friend_pizzas.append('hawaiian')

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

print(f"\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
