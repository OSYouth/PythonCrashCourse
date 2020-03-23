pizzas = ['BSK', 'LKS', 'ZZ']
friend_pizzas = pizzas[:]

pizzas.append("new")
friend_pizzas.append("unknown")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)