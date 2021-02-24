from die import Die

die6 = Die()
for t in range(1, 11):
    print(str(t) + " - ", end='')
    die6.roll_die()
print()

die10 = Die(10)
for t in range(1, 11):
    print(str(t) + " - ", end='')
    die10.roll_die()
print()

die20 = Die(20)
for t in range(1, 11):
    print(str(t) + " - ", end='')
    die20.roll_die()