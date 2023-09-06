pet_1 = {
    'name': 'ted',
    'breed': 'boxer',
    'owner': 'fernanda'
}

pet_2 = {
    'name': 'cookie',
    'breed': 'cocker spaniel',
    'owner': 'enzo'
}

pet_3 = {
    'name': 'atenea',
    'breed': 'husky',
    'owner': 'pablo'
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"It's name is {pet['name'].title()}.")
    print(f"It's a {pet['breed'].title()}.")
    print(f"The owner is {pet['owner'].title()}.\n")\
