pets = {
    'pet_1': {
        'name': 'ted',
        'breed': 'boxer',
        'owner': 'fernanda',
},
    'pet_2': {
        'name': 'cookie',
        'breed': 'cocker spaniel',
        'owner': 'enzo',
},
    'pet_3': {
        'name': 'atenea',
        'breed': 'husky',
        'owner': 'pablo',
},
}

for pet, info in pets.items():
    name = info['name'].title()
    breed = info['breed'].title()
    owner = info['owner'].title()

    print(f"It's name is {name}.")
    print(f"\tIt is a {breed}.")
    print(f"\tThe owner's name is {owner}.\n")