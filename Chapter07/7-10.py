holiday_resorts = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    resort = input("If you could visit one place in the world, where would you go? ")
    holiday_resorts[name] = resort

    repeat = input("would you like to invite other person to poll?(yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n---- Poll Results ----")
for name, resort in holiday_resorts.items():
    print(name.title() + " would like to visit " + resort +".")